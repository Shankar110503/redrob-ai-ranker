import gzip
import json
import pandas as pd
import numpy as np

def run_ranking(candidates_file_path, output_file_path):
    print("कैंडिडेट्स डेटा लोड हो रहा है...")
    candidates = []
    
    # gzipped या नॉर्मल jsonl फाइल दोनों को रीड करने के लिए
    open_func = gzip.open if candidates_file_path.endswith('.gz') else open
    mode = 'rt' if candidates_file_path.endswith('.gz') else 'r'
    
    with open_func(candidates_file_path, mode, encoding='utf-8') as f:
        for line in f:
            if line.strip():
                candidates.append(json.loads(line))
                
    print(f"कुल {len(candidates)} कैंडिडेट्स मिले। प्रोसेसिंग शुरू...")
    
    scored_candidates = []
    
    # JD के मुख्य कीवर्ड्स
    jd_keywords = {'embedding', 'retrieval', 'ranking', 'llm', 'vector', 'nlp', 'search'}
    
    for cand in candidates:
        cid = cand.get('candidate_id')
        
        # 1. हनीपॉट फ़िल्टर (Honeypot Trap Detection)
        # उदाहरण: अनुभव कंपनी की स्थापना से ज्यादा होना, या बिना अनुभव के ढेरों स्किल्स
        exp_years = cand.get('experience_years', 0)
        skills = cand.get('skills', [])
        
        # सामान्य हनीपॉट रूल्स (डेटासेट के आधार पर इसे बदला जा सकता है)
        if exp_years > 20 or (len(skills) > 15 and exp_years == 0):
            continue # इसे छोड़ दें (टियर 0)
            
        # 2. रोल के लिए योग्यता स्कोर (JD Match Score)
        # 5-9 साल का अनुभव बेस्ट माना गया है
        exp_score = 0
        if 5 <= exp_years <= 9:
            exp_score = 10
        elif 3 <= exp_years < 5 or 9 < exp_years <= 12:
            exp_score = 6
        else:
            exp_score = 2
            
        # कीवर्ड मैचिंग (सिस्टम्स को समझना, न कि सिर्फ फ्रेमवर्क्स)
        skills_text = " ".join([s.lower() for s in skills])
        keyword_matches = sum(1 for kw in jd_keywords if kw in skills_text)
        
        # 3. बिहेवियरल सिग्नल्स मॉडिफायर (Redrob Behavioral Signals)
        signals = cand.get('redrob_signals', {})
        response_rate = signals.get('recruiter_response_rate', 0.0)
        notice_period = signals.get('notice_period_days', 90)
        
        # जो कैंडिडेट 6 महीने से एक्टिव नहीं हैं या रिस्पॉन्स नहीं दे रहे, उन्हें कम स्कोर दें
        activity_multiplier = 1.0
        if response_rate < 0.10: 
            activity_multiplier *= 0.5
        if notice_period <= 30: # कम नोटिस पीरियड को प्राथमिकता
            exp_score += 3
            
        # फाइनल कंपोजिट स्कोर गणना
        base_score = (exp_score * 2) + (keyword_matches * 1.5)
        final_score = round(base_score * activity_multiplier, 4)
        
        # स्वचालित रीज़निंग जनरेशन (वैविध्यपूर्ण और विशिष्ट)
        reasoning = f"Experienced engineer with {exp_years} years in relevant tech stack. Strong behavioral signals with {int(response_rate*100)}% recruiter response rate."
        if notice_period <= 30:
            reasoning += " Advantageous short notice period."
            
        scored_candidates.append({
            'candidate_id': cid,
            'score': final_score,
            'reasoning': reasoning
        })
        
    # डेटाफ्रेम बनाएं और सॉर्ट करें
    df = pd.DataFrame(scored_candidates)
    
    # नियम 3: पहले स्कोर के आधार पर (घटते क्रम में), फिर टाइब्रेकर के लिए candidate_id (बढ़ते क्रम में)
    df = df.sort_values(by=['score', 'candidate_id'], ascending=[False, True])
    
    # केवल टॉप 100 कैंडिडेट्स चुनें
    top_100 = df.head(100).copy()
    
    # रैंक कॉलम असाइन करें (1 से 100)
    top_100['rank'] = range(1, 101)
    
    # कॉलम का सही क्रम व्यवस्थित करें
    output_df = top_100[['candidate_id', 'rank', 'score', 'reasoning']]
    
    # CSV में सेव करें (UTF-8 एन्कोडिंग)
    output_df.to_csv(output_file_path, index=False, encoding='utf-8')
    print(f"सफलतापूर्वक टॉप 100 की फाइल '{output_file_path}' पर सेव हो गई है!")

if __name__ == "__main__":
    # आप इसे अपने फाइल पाथ के हिसाब से रन कर सकते हैं
    run_ranking('candidates.jsonl.gz', 'team_shankar.csv')
  

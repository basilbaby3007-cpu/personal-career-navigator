import requests

url = 'http://localhost:8001'
try:
    r = requests.get(url, timeout=3)
    print('root status', r.status_code, r.json())
except Exception as e:
    print('root error', e)

try:
    profile = {'resume_text':'I know python, sql', 'dream_role':'ml_engineer', 'hours_per_week':10, 'current_skills':['python']}
    r = requests.post(url+'/api/roadmap', json=profile, timeout=3)
    print('roadmap', r.status_code, r.json())
except Exception as e:
    print('roadmap error', e)

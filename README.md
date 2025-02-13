# socia_media_app_final
## Instructions to run the project
1.to create virtual environment run the command python -m venv venv
2.now to activate venv we will run the command venv\Scripts\activate
3.now we will install requirements by running command pip install -r requirements.txt
4.intialize the database first change the directory using command:cd shared then use commands:flask db init
                                                                                              flask db migrate
                                                                                              flask db upgrade

5.then we will rollback to main directory by using command :cd..
6.then we will run our application using command python app_runner.py
7.these are my credential for the firebase cloud storage {
  "type": "service_account",
  "project_id": "social-media-app-61969",
  "private_key_id": "e520fa4dcf736a9c2171b1396948320b78c11e9e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCscA5Nm6g53Hy5\nJpGFyV/pQ6xA/l93+fWmUESkmNi8jqgPi13fObPb51IpKUpsGXNN+1uhNYv1Z+sw\nJWf0YJt+jzUSMMicMcx5scqw/FhKcWPQG0w8yQeBv1xTyWPR5jrgPJVKWzEuwR8b\nkyeFJVC1KcazSgD/JhMe8N9pcZB/4SOZGgbp6weROR4JDQjkYEDpitxjW1CFNGE6\nifpxEIBeBndx52i6Q0hh7vgZhuphYhryGDCCGQ40nSOOv4cK2hm32F7jKVP5UrD2\ng0hjVrGXuG2xGz+UIMSA72JDwNcXuLic5zYgSMz3gu6DBw9fcEKPjjcs0dfeNGo8\nXq2sFTiNAgMBAAECggEAGOiP3FyLgp4rowgj9bYmxVh56aKE8lz4Q8es/rS4fBZE\nRwiL7QqWBUInH1yATFipy/4u2HzWZILYGYqRt158H546nY/P7qYP4hVRUNsGuuwh\nraY/zzj/vVmB0fWRlniiERGXRBgjpNwPLQnG5+gBvkWUVwIt3i1nDi1frEjUBXCo\njdNXSeGew5H711eiq9lG+nb+ldFKIwOS72Er3FJBk5dUER1iZcz2fFs+oIgHr+JY\nPxpeDhmxwhuk0ENvDA+UBz6HqtjTtmfWzCtQp9NNLvjWwb7d/oy01lOzdZgiKO8m\nGsGQvBLRcYZkSGiEzExgdf9Ct51ZcBNcXjPmK3xSqQKBgQDddSJxZZsnZehtkKne\nbqocA4/ASZBIvoli8MPrfxjupaYliDROoHnAjXXULbtO07cY+5+MpkpW9vO2v6RT\nODCBH0fXo36+xZALX7zmMhYkMNakiVaMYvfuN+BWcRkuj3TTBsYojGcdwueazqyl\no7oaaO8yr1ZUPyOWSfD4IywNmQKBgQDHVYt0Fj8o5nrUd8eQ0+nrtiM2M43Sbyk6\nENjroqEgG3lq3hDshDOKgxPH0LVhREL3fEPq2f7lHAYx3d8Lu7bFF3UoTP3PTWv8\nNgks4cwP1qHre59O0jIwnJBAf966siiR36pP0fELNqOstIcNxmpbmgmJeP+bMMRM\n8CEoGDvTFQKBgDmeDy8Hq31tozJWcAvCKRoOxyjVOufiQuZuE9tCfx8gFAEx1cIb\nOHIjm+NvXotcxAeI9/LlFPRZXgFPDRblyKDfnZZ6IDDMP/TlnMUbhO03k7DNVqpB\n2ZWuDf0Pgei+RDvfSFEmbnGs0wtQ+FREK9hRMuKyAbj7kGu6oyo8JGsJAoGARoMl\nTJBeEUrOooAokTvVYLNSa2b7QThfXhH9mgUyeBgf8ETTucbeMJ5DjghvURQDmGZV\n5CrvNv6d1mAE+bKSac/teq8ZjY52p4Y54q2RMP0c1B8r8Ib8iCOqB5b0JBjHrypu\npcO/P9c5OOu3ZpEMqJCp1P5/dNdgaVL8d6Fy8C0CgYEAyFKtvJyf3eNiB5T7CW89\nWncVCna46FyjhmUG8E+ISnVczmzhfauICo1dF/A6CxGfgX6B+DUbzx55HeyvSkeD\nPBn9cdd1GiA40ga12hY7zQkhR0GFltUlaCBjPfs7RbqcBoD8RWb+H4zkkJ3YtqMA\nsYqtW2XGqHwwejjpGZbkbCk=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-qyckq@social-media-app-61969.iam.gserviceaccount.com",
  "client_id": "102480037765860040474",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qyckq%40social-media-app-61969.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

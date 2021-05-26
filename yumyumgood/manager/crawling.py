import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://mportal.cau.ac.kr/main.do?isLoginFail=false&errorMsg=&idTagName=userID&pwdTagName=password&credTagName=credType&returnUrlTagName=retURL&logoffUrl=https%3A%2F%2Fsso2.cau.ac.kr%2FSSO%2FAuthWeb%2FLogoff.aspx%3Fssosite%3Dmportal.cau.ac.kr%26retURL%3Dhttp%253A%252F%252Fmportal.cau.ac.kr%252Fmain.do%253FredirectUrl%253Dhttps%253A%252F%252Fmportal.cau.ac.kr%252Fmain.do&logonUrl=https%3A%2F%2Fsso2.cau.ac.kr%2FSSO%2FAuthWeb%2FLogon.aspx%3Fssosite%3Dmportal.cau.ac.kr&returnUrl=")
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup.find_all(attrs={'class':'ng-scope'}))
import requests
from bs4 import BeautifulSoup


def open_file():                # Function to open the file that containn the view page source for  url = http://www.edudel.nic.in/mis/schoolplant/frmDistrictAndSchoolInformation.aspx after selecting school
    fr=open("PageSource.txt",'r')
    content=fr.read()
    txt=content.encode('utf-8')      #convert the string to bytes
    soup=BeautifulSoup(txt,"html.parser")
    main_table=soup.find("table",{'class':'MISlabel'})   # get the main table
    for row in main_table.find_all("tr"):
        eachcell = row.find_all("td")
        url="http://www.edudel.nic.in/mis/schoolplant/frmSchoolInformation.aspx?Schoolid="+eachcell[2].string    #url for each school information page
        visit_each_school_info_page(url)

def visit_each_school_info_page(url):
    school_info=[]
    response=requests.get(url)
    txt=response.content
    soup=BeautifulSoup(txt,"html.parser")
    school_name=soup.find('span',{'id':'lblschname'})
    school_info.append(school_name.string)
    school_address=soup.find('span',{'id':'lbladdress'})
    school_info.append(school_address.string)
    school_emailid=soup.find('span',{'id':'lblem'})
    school_info.append(school_emailid.string)
    print(school_info)





#url="http://www.edudel.nic.in/mis/schoolplant/frmDistrictAndSchoolInformation.aspx"
#get_names(url)
open_file()
#test()

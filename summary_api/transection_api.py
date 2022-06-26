from asyncio.windows_events import NULL
import numpy as np
from pandas import DataFrame
#-------------------------------Transection API---------------------------------------#
def csc_many(df):
  n_CSC = [1 if i == 'CSC' else 0 for i in df['dsc_role']]
  df['Number of CSCs']= n_CSC
  #Inactive CSCs
  #csc_active_status >"0"
  # Inactive_CSCs = [1 if i > 0 else 0 for i in df['csc_active_status']]
  # df['Inactive_CSCs']= Inactive_CSCs
  #Transacting Active CSCs (Time Period)
  #csc_active_status  <= "0" and id : *
  #Transacting_CSCs = [1 if df['csc_active_status'][i] <= 0 and df['application_id'][i] else 0 for i in range len(df)]
  # df['Transacting Active CSCs (Time Period)']= Transacting_CSCs

  result=df.groupby('application_district').aggregate({'Number of CSCs':'sum', 
                                          'application_status': 'count'
                                          })
  result.reset_index(inplace=True)
  result['Total Transaction (Time Period)']=result['application_status']
  result.rename(columns = {'application_district':'Name of Districts'}, inplace = True)
  result.rename(columns = {'application_status':'Total Application'}, inplace = True)
  return result.to_dict(orient = 'records')



#Application disposed after time limit(Module-Application disposed after time limit)
def Application_disposed_after_time_limit_Module_Application(df):

  #df = DataFrame(list(df))

  comp = [1 if i == 'COMPLETED' else 0 for i in df['application_status']]
  df['completed']= comp
  # application status  = complete

  days_list =  ["Within limit 17-30 days","Within limit 08-16 days",
                  "Within limit 01-07 days", "Within limit 30 or more days"]

  within_limit_total=[]
  for i in range(len(df)):
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] in days_list):
      within_limit_total.append(1)
    else: within_limit_total.append(0)

  df['Within Limits'] = within_limit_total
  # Approval within time limit
  # application_status.keyword : "COMPLETED" 
  # and within_limit.keyword : "Within limit 17-30 days"  
  # or within_limit.keyword : "Within limit 08-16 days" 
  # or within_limit.keyword : "Within limit 01-07 days"  
  # or within_limit.keyword : "Within limit 30 or more days"

  within_a = []
  within_b = []
  within_c = []
  within_d = []
  beyond_lmt=[]
  for i in range(len(df)):
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 01-07 days"):
      within_a.append(1)
    else: within_a.append(0)
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 08-16 days"):
      within_b.append(1)
    else: within_b.append(0)
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 17-30 days"):
      within_c.append(1)
    else: within_c.append(0)
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 30 or more days"):
      within_d.append(1)
    else: within_d.append(0)
    if (df['completed'].iloc[i] == 1) and (df['beyond_limit'].iloc[i] == "Yes"):
      beyond_lmt.append(1)
    else: beyond_lmt.append(0)  

  df['1 to 7 days'] = within_a
  df['8 to 16 days'] = within_b
  df['17 to 30 days'] = within_c
  df['30 or more days'] = within_d
  df['Application disposal beyond time limit']=beyond_lmt

  DATA = df.groupby('application_district').aggregate({'application_status':'count', 
                                          'Within Limits': 'sum',
                                          'Application disposal beyond time limit':'sum',
                                          '1 to 7 days': 'sum',
                                          '8 to 16 days': 'sum',
                                          '17 to 30 days': 'sum',
                                          '30 or more days': 'sum'})
  DATA.reset_index(inplace=True)
  DATA.rename(columns = {'application_district':'Name of Districts'}, inplace = True)
  DATA.rename(columns = {'application_status':'Total Application'}, inplace = True)
  
  return DATA.to_dict(orient = 'records')









#Aging summary department wise(Module-Aging summary report)
def Aging_summary_department_wise(df):

  #df = DataFrame(list(df))

  pen = [1 if i == 'PENDING_ENROLLMENT' or i== 'PENDING_VERIFICATION' else 0 for i in df['application_status']]
  df['Pending'] = pen

  comp = [1 if i == 'COMPLETED' else 0 for i in df['application_status']]
  df['completed']= comp
  # application status  = complete

  days_list =  ["Within limit 17-30 days","Within limit 08-16 days",
                  "Within limit 01-07 days", "Within limit 30 or more days"]

  within_limit_total=[]
  for i in range(len(df)):
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] in days_list):
      within_limit_total.append(1)
    else: within_limit_total.append(0)

  df['Within Limits'] = within_limit_total
  # Approval within time limit
  # application_status.keyword : "COMPLETED" 
  # and within_limit.keyword : "Within limit 17-30 days"  
  # or within_limit.keyword : "Within limit 08-16 days" 
  # or within_limit.keyword : "Within limit 01-07 days"  
  # or within_limit.keyword : "Within limit 30 or more days"

  within_a = []
  within_b = []
  within_c = []
  within_d = []

  for i in range(len(df)):
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 01-07 days"):
      within_a.append(1)
    else: within_a.append(0)
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 08-16 days"):
      within_b.append(1)
    else: within_b.append(0)
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 17-30 days"):
      within_c.append(1)
    else: within_c.append(0)
    if (df['completed'].iloc[i] == 1) and (df['within_limit'].iloc[i] == "Within limit 30 or more days"):
      within_d.append(1)
    else: within_d.append(0)  

  df['1 to 7 days'] = within_a
  df['8 to 16 days'] = within_b
  df['17 to 30 days'] = within_c
  df['30 or more days'] = within_d

  DATA = df.groupby('department').aggregate({'Pending':'sum', 
                                          'Within Limits': 'sum',
                                          '1 to 7 days': 'sum',
                                          '8 to 16 days': 'sum',
                                          '17 to 30 days': 'sum',
                                          '30 or more days': 'sum'})

  return DATA.reset_index().to_dict(orient = 'records')









#Transactional Details
def T_Details(df):
  df['application_id'] = df['application_id'].fillna(0).astype(int)
  result=df[['application_id','applicant_name','office_name','application_district','dsc_name','application_status','due_date']]
  
  
  result.due_date = result.due_date.apply(lambda x: x.date())
  result.rename(columns = {'application_id':'Application Ref No'}, inplace = True)
  result.rename(columns = {'applicant_name':'Applicant'}, inplace = True)
  result.rename(columns = {'office_name':'Name of Office'}, inplace = True)
  result.rename(columns = {'application_district':'District'}, inplace = True)
  result.rename(columns = {'dsc_name':'Initiated By'}, inplace = True)
  result.rename(columns = {'application_status':'Status'}, inplace = True)
  result.rename(columns = {'due_date':'Due Date'}, inplace = True)

  
  result = result.fillna('')
  return result.to_dict('records')







#District Wise & Service Wise
def District_Wise_Service_Wise(df):
    x=df.scheme_name.unique()
    y=df.application_district.unique()
    #first value is null
    y=y[1::]
    
    #y=y.dropna()
    d={}
    df2 = DataFrame()
    df2['Service Name']=x
    z=0
    for i in y:
      if i!='None':
        for k in x:
          if k!='None':
                d[k]=0
            
          
        for j in range(len(df)):
            if df['application_district'][j]==i:
                d[df['scheme_name'][j]]+=1
                
        df2[i]=''
        q=0
        for z in x:
          if z!='None':
            df2[i][q]=d[z]
            q+=1
    
    return df2.to_dict('records')








#Division wise transaction Reports

def Division_wise_transaction_Reports(df):

  #df = DataFrame(list(df))
  comp = [1 if i == 'COMPLETED' else 0 for i in df['application_status']]
  df['Approved']= comp
  # application status  = completed
  
  temp = [1 if i == '13' else 0 for i in df['application_status']]
  df['Temp Approved']= temp
  # application status  = complete

  rej = [1 if i == 'REJECTED' else 0 for i in df['application_status']]
  df['Rejected']= rej

  pen = [1 if i == 'PENDING_ENROLLMENT' or i=='PENDING_VERIFICATION' else 0 for i in df['application_status']]
  df['Total Pending']= pen

  sentback = [1 if i == '16' else 0 for i in df['application_status']]
  df['Sent Back']= sentback
  
  # days_list =  ["Within limit 17-30 days","Within limit 08-16 days",
  #               "Within limit 01-07 days", "Within limit 30 or more days"]

  # within_limit_total = []
  beyond_limit_total = []
  for i in range(len(df)):
    # if (df['Approved'].iloc[i] == 1) and (df['within_limit'].iloc[i] in days_list):
    #   within_limit_total.append(1)
    # else: within_limit_total.append(0)

    if (df['Total Pending'].iloc[i] == 1) and (df['beyond_limit'].iloc[i] == 'Yes'):
      beyond_limit_total.append(1)
    else: beyond_limit_total.append(0)

  df['Beyond Limit (Pending)'] = beyond_limit_total
  #df['Approval within time limit'] = within_limit_total


  results = df.groupby('division').aggregate({'application_status':'count',
                                                'Approved':'sum',
                                                'Temp Approved':'sum',
                                                'Sent Back': 'sum',
                                                'Rejected':'sum',
                                                'Total Pending':'sum',
                                          
                                                'Beyond Limit (Pending)':'sum'})
  
  # print(len(results))
  results = results.reset_index()
  l=[]
  for i in range(len(results)):
    l.append(round((results['Beyond Limit (Pending)'][i]/results['application_status'][i])*100,2))
  results['Beyond Limit (Pending)%']=l
  results.rename(columns = {'application_status':'Total_Application'}, inplace = True)
  # results['Beyond Limit (Pending) %'] = (results['Beyond Limit (Pending)'] / results['application_status']) * 100
  # results.fillna(0, inplace = True)
  #print(results)
  DATA= results.to_dict('records')
  
  return DATA


#Application Summary Department Wise(Module-Summary Report)
def Application_Summary_Department_Wise(df):
  #df = DataFrame(list(df))
  comp = [1 if i == 'COMPLETED' else 0 for i in df['application_status']]
  df['Approved']= comp
  

  rej = [1 if i == 'REJECTED' else 0 for i in df['application_status']]
  df['Rejected']= rej

  pen = [1 if i == 'PENDING_ENROLLMENT' or i=='PENDING_VERIFICATION' else 0 for i in df['application_status']]
  df['Pending']= pen
  
  results = df.groupby('department').aggregate({  'application_status':'count', 
                                                'Approved':'sum',
                                                'Rejected':'sum',
                                                'Pending':'sum',
                                               }) 

                                            
  results.reset_index(inplace = True) 
  results.rename(columns = {'application_status':'Total_Application'}, inplace = True)
  results.rename(columns = {'department':'Name of department'}, inplace = True)
  return results.to_dict('records')



#transection_api-->CSC transactions(3 clm)
def CSC_transactions_with_3_col(df):
# count application id for total transection 
  results = df.groupby(['application_district','scheme_name']).aggregate({
                                                 'application_id':'count',
                                               })
                                                                        
  results.reset_index(inplace = True) 
  # name according to table
  results.rename(columns = {'scheme_name':'Service Name'}, inplace = True)
  results.rename(columns = {'application_district':'Name of Districts'}, inplace = True)
  results.rename(columns = {'application_id':'Transection Count'}, inplace = True)

  return results.to_dict('records')



#transection_api-->Deity_Report
def Deity_Report(df):

  #lsk value and chips user present in dsc_role field
  lsk = [1 if i=='Service Access Provider(LSK)' else 0 for i in df['dsc_role']]
  df['Service Access Provider(LSK)']= lsk
  chps = [1 if i=='CHiPS User' else 0 for i in df['dsc_role']]
  df['CHiPS User']= chps
  # sum of completed and rejected as a redress field
  readress = [1 if i == 'COMPLETED' or i=='REJECTED' else 0 for i in df['application_status']]
  df['Redresses(Approved + Rejected)']= readress
  
  results = df.groupby('scheme_name').aggregate({
                                                 'CHiPS User':'sum',
                                                'Service Access Provider(LSK)':'sum',
                                                'Redresses(Approved + Rejected)':'sum'
                                

                                            })
  results.reset_index(inplace = True) 
  
  #results.rename(columns = {'SCHEME_NAME':'Name of Service'}, inplace = True)
  #results.rename(columns = {'APPLICATION_DISTRICT':'Name of Districts'}, inplace = True)
  return results.to_dict('records')



def No_of_lsk_district_wise(df):
  comp = [1 if i=='Service Access Provider(LSK)' else 0 for i in df['dsc_role']]
  df['No of lsk']= comp
  

  results = df.groupby('application_district').aggregate({ 
                                                'No of lsk':'sum',
                                                
                                

                                            })
  results.reset_index(inplace = True) 
  
  #results.rename(columns = {'SCHEME_NAME':'Name of Service'}, inplace = True)
  results.rename(columns = {'application_district':'Name of Districts'}, inplace = True)
  return results.to_dict('records')





def App_disposed_after_time(df):

  #df = DataFrame(list(df))
  comp = [1 if df['application_status'][i] == 'COMPLETED' else 0 for i in range (len(df['application_status']))]
  df['Approved Beyond SLA']= comp
  

  rej = [1 if df['application_status'][i] == 'REJECTED' else 0 for i in range (len(df['application_status']))]
  df['Rejected Beyond SLA']= rej

  #unique_f = lambda x: np.unique(x)[0]
  results = df.groupby('scheme_name').aggregate({ 
                                                'Approved Beyond SLA':'sum',
                                                'Rejected Beyond SLA':'sum',
                                

                                            })
  results.reset_index(inplace = True) 
  
  results.rename(columns = {'scheme_name':'Name of Service'}, inplace = True)
  #print(sum(df['Approved Beyond SLA']))
  #results.rename(columns = {'APPLICATION_DISTRICT':'Name of Districts'}, inplace = True)
  return results.to_dict('records')
  #-------------------------end of transection API-------------------------#


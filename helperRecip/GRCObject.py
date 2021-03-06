'''
Created on Jul 20, 2013

@author: diana.tzinov

'''

from Elements import Elements

class GRCObject(object):
    elem = Elements()
    
    contract_elements = {
                        "title":elem.object_title,   
                         "owner":elem.object_owner, 
                        "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    contract_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
    
        
    #CONTROL
    control_elements = {
                        "title":elem.object_title,   
                         "owner":elem.object_owner, 
                         "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code,
                        "kind":elem.object_dropdown,
                        "fraud_related":elem.object_dropdown,
                        "key_control":elem.object_dropdown,
                        "means":elem.object_dropdown
                        } 
 
    
    
    control_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code",
                      "kind":2,
                      "fraud_related":2,
                      "key_control":2,
                      "means":2
                      }
    
    
    
    #DATA ASSET
    data_asset_elements = {
                        "title":elem.object_title,   
                        "owner":elem.object_owner,  
                         "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    data_asset_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
    
    #FACITY
    facility_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner,  
                         "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    facility_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
    
    #MARKET
    market_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner,  
                         "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    market_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
    
    
    #ORGGROUPS
    org_group_elements = {
                        "title":elem.object_title,    
                        "owner":elem.object_owner,
                         "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    org_group_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
        #POLICY
        
    policy_elements = {
                        "title":elem.object_title, 
                        "owner":elem.object_owner, 
                         "description":elem.object_iFrame,  
                        "url":elem.object_url,
                        "code":elem.object_code,
                        "kind":elem.object_dropdown
                        #"kind":elem.object_kind
                        } 
 
    
    
    policy_values = {
                      'title':"",  
                       'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                       "code":"auto-populated-code",
                       "kind":1
                      }
    
    
    #PROCESS
        
    process_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner,
                       "description":elem.object_iFrame,  
                        "url":elem.object_url,
                        "code":elem.object_code,
                         "notes":elem.object_iFrame,
                         "network_zone":elem.object_dropdown,
                        } 
 
    
    
    process_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code",
                      "notes":"",
                      "network_zone":2
                      }
    
    #POLICY
        
    product_elements = {
                        "title":elem.object_title, 
                        "owner":elem.object_owner, 
                         "description":elem.object_iFrame,   
                        "url":elem.object_url,
                        "code":elem.object_code,
                        "type":elem.object_dropdown
                        #"kind":elem.object_kind
                        } 
 
    
    
    product_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code",
                      "type":2
                      }
    
    
    #PROGRAM
    
    
    program_elements = {
                        "title":elem.object_title,  
                         "owner":elem.object_owner,  
                        "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code,
                        "scope":elem.object_scope,
                        "organization":elem.object_organization
                        } 
 
    
    
    program_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code",
                      "scope":"",
                      "organization":""
                      }
    

    #PROJECT
        
    project_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner,
                         "description":elem.object_iFrame,  
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    project_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }

    
    #REGULATION
    regulation_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner,  
                        "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    regulation_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
    
       #OBJECTIVE
    objective_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner,  
                        "description":elem.object_iFrame,
                        "url":elem.object_url,
                        "code":elem.object_code
                        } 
 
    
    
    objective_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code"
                      }
    
    
  
    #System
        
    system_elements = {
                        "title":elem.object_title,  
                        "owner":elem.object_owner, 
                       "description":elem.object_iFrame, 
                        "url":elem.object_url,
                        "code":elem.object_code,
                        "notes":elem.object_iFrame,
                         "network_zone":elem.object_dropdown,
                        "network_zone":elem.object_dropdown
                        } 
 
    
    
    system_values = {
                      'title':"",  
                      'owner':"",
                      "description":"",
                      'url': "http://www.google.com", 
                      "code":"auto-populated-code",
                      "notes":"",
                      "network_zone":2
                      }
    
    
    
    program_map_to_lhn = ["Regulation", "Contract", "Policy", "Control", "Objective", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group"]


    program_map_to_widget = ["Regulation", "Contract", "Policy", "Control", "Objective", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group", "Person", "Document"]


#LHN GOVERNANCE OBJECTS
    
    regulation_map_to_lhn = ["Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    
   

    contract_map_to_lhn =  ["Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    
    control_map_to_lhn =  ["Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    
    policy_map_to_lhn = ["Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    

    
    
    objective_map_to_lhn = ["Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    
#BUSINESS OBJECT LHN
    
    system_map_to_lhn = ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "Process", "Data", "Product", "Project", "Facility", "Market", "Group"]
    
    process_map_to_lhn = ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Data", "Product", "Project", "Facility", "Market", "Group"]
    
    data_asset_map_to_lhn = ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Process", "Product", "Project", "Facility", "Market", "Group"]
    
    product_map_to_lhn = ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Process", "Data", "Project", "Facility", "Market", "Group"]
    
    project_map_to_lhn = ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Process", "Data", "Product", "Facility", "Market", "Group"]
    
    facility_map_to_lhn = ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Process", "Data", "Product", "Project", "Market", "Group"]
    

    market_map_to_lhn= ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Process", "Data", "Product", "Project", "Facility", "Group"]
    
    org_group_map_to_lhn= ["Program", "Regulation", "Contract", "Policy", "Control", "Objective", 
                        "System", "Process", "Data", "Product", "Project", "Facility", "Market"]
    
    
#WIDGET GOVERNANCE OBJECTS
    regulation_map_to_widget = [#"Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"]
    
    contract_map_to_widget = [#"Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    
    policy_map_to_widget = [#"Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    
    control_map_to_widget = [#"Program", 
                          "System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          #"Contract", "Policy", "Control", "Objective"
                          ]
    objective_map_to_widget = [#"Program", 
                          "Objective", "Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          #"Contract", "Policy", "Control", "Objective"
                          ]

#WIDGET BUSINESS OBJECTS

    system_map_to_widget = [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    
    process_map_to_widget = [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    
    data_asset_map_to_widget= [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    
    product_map_to_widget= [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    project_map_to_widget= [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    
    facility_map_to_widget= [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    
    market_map_to_widget= [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    
    org_group_map_to_widget= [#"Program", "Regulation", "Contract", "Policy",
                          "Section","Objective","Control","System", "Process", "Data", "Product", "Project", "Facility", "Market", "Group","Person", "Document"
                          ]
    

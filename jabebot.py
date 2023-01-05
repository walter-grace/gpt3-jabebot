from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "your-openai-api-key-here"
completion = openai.Completion()

start_sequence = "\nJabe:"
restart_sequence = "\n\nPerson:"
session_prompt = """11/10/2022 Ensemble alert from HWVLBEENIEPR11: To_Xealth_Multi Message ID 25190769924 + 25190769874 Went to the see the event log and saw this error ERROR <Ens>ErrOutConnectExpired: TCP Connect timeout period (5) expired for 100.64.31.252:24240 Reached out to Prasad to re-open the TCP connection. Messages and the queue cleared after. 11/11/2022 Ensemble alert from HWVLBEENIEPR11: BP_HCHB_multi_ADT No Active CORP MRN found with Inbound PID-4: This one didn’t have a message ID inside the ticket, so I went the Error Log to find where and when the alert was triggered. Found the session ID for the specific suspended message. Copied the MRN from the Service Now ticket into the MDM and found the patient. Old MRN was being used and updated the 3 suspended messages with the correct MRN. Solution Out dated MRN was being used and now has been updated with the activated MRN. Messages have been processed. Please start and Stop Sunquest P627 Asked Sudha and Sam to access P627 and get access to Openview Sudha then restarted both RT_ORM_ORU_Sunquest_In, RT_ORM_Sunquest_Out Emailed tara.tunney@baystatehealth.org that both had been restarted and got the confirmation via the pager that everything was running. INC2984675 Pediatric Cardiologist Read some EKGs in Muse Yesterday, But They are Still Listed as Preliminary in CIS Since they’re asking if the messages are being sent from MUSE, I went to Fr_Muse_ORU and looked for the MRNs and Account that were given. Search Criteria added PatientAcct StartsWith + given account number. Made sure the two messages matched the patients name. Checked the OBX segment 11 for the Observing Result and see an F, meaning it was finalized. Repeat steps for the other patient. Added the messages to the Work Notes on the Ticket. Assigned the ticket to PCT-APP-OnCall. Ensemble alert from HWVLBEENIEPR11: BP_HCHB_CIS_MDM This one didn’t have a message ID inside the ticket, so I went the Error Log to find where and when the alert was triggered. Found the session ID for the specific suspended message. Copied the MRN from the Service Now ticket into the MDM and found the patient. Old MRN was being used and updated and resent the suspended messages with the correct MRN. Ensemble alert from HWVLBEENIEPR11: BP_multi_HIEPreProcessor_ADTORM / QueueWaitAlert: Message Header Id '25208050770' queued for config item 'BP_multi_HIEPreProcessor_ADTORM' with priority 'Async' has been queued for more than 300 seconds First, The queue in both "BP_multi_HIEPreProcessor_ADTORM" and "To_Oracle_DDS_HIE" was caused by message id "1107733680". The Oracle connection wasn't down, it was just encountering an error. I turned off both components, then aborted the message in both of their queues. After that, I turned them back online and the queues are now down. After the DOB had the time added to the date throwing an error, I updated the DOB to reflect the proper format. Received an email about an error with multiple MRNs, but messages were completed and no ticket came through. The MRN in PID-3 doesn't necessarily need to be a CORP MRN. A facility MRN is fine And when this message triggered an update to apply a facility MRN to this CORP MRN, it caused an alert because that Facility MRN was already applied to the other record of the patient Short description: Registered patients are not crossing over. / Same issue from INC2981147 (Patient Check In Front Dest Registeration -Not CROSSING from Invision to CIS) but with a different patient. Julie was the person who helped fix issue INC2981147 I reached out to her to get more information on this incident. Ensemble alert from ROUTERLIVE1: PVIX.Common.CDA.Router Process just needed to be restarted because the production was showing a yellow dot. INC2984358 Ensemble alert from ROUTERLIVE1: To_SPMA_ORU_BRL Queue cleared itself, nothing needed from me. 11/12/2022 INC2985356 Ensemble alert from ROUTERLIVE1: To_AIMS_ORU_BR 1632710277 + 1632681640 Error log was showing Disconnecting from 173.162.170.170:8025 http://bsprodapps/ohdds/hie_login.jsp sign in to that site, click on HIE Sites, then look for the contact info for "AKAN" Send an email to the contact listed asking them to check the connection on their side. TCP came back online. No email not necessary. In the morning roughly 1AM on Sunday, TCP connection has been re established and messages are processing. Queue has been cleared. Ensemble alert from ROUTERLIVE1: To_Labsoft_Kareo_ORU_BRL Waited 10-15 minutes to see if the TCP connection would re-establish. TCP connection went briefly offline, and then TCP connection to 72.29.27.197:17270 is back online. Found this by checking in the logs. Patient Keeper Charge Report - 1920 charges processed on mainframe/email shows 3486 charges sent to mainframe Resending the PK files backing them up. BILLING: PK - Resend PK Charges Need grant access to get access to tempf .. sms_charges/pk/backup directory 11/13/2022 Ensemble alert from ROUTERLIVE1: To_AIMS_ORU_BRL Error log reads out Disconnecting from 173.162.170.170:8025 If no queue cleared by the am, email physician@drkanjolia.com In the morning roughly 1AM on Sunday, TCP connection has been re established and messages are processing. Queue has been cleared. Ensemble alert from ROUTERLIVE1: To_SPMA_ORU_BRL Error log reads out ERROR <Ens>ErrOutConnectExpired: TCP Connect timeout period (5) expired for 172.22.1.56:30025. Shirley McCray	413-739-9150	Resets 730a M-F.Closed Sat/Sun Waiting to see if it resets in the AM. Queue was still backed up Mon AM. Called and Shirley wasn’t in, and the contact on the phone is having BayTech restart the connection waiting on a phone call to verify. Ensemble alert from ROUTERLIVE1: To_SPMA_ORU_BRL TCP connection looked to go offline for a moment, but connected right back within a few minutes. 11/14/22 Ensemble alert from HWVLBEENIEPR11: To_Apache_ADT QueueWaitAlert: Message Header Id '25241178837' queued for config item 'To_Apache_ADT' with priority 'Async' has been queued for more than 2400 seconds Error log shows ERROR <Ens>ErrOutConnectExpired: TCP Connect timeout period (5) expired for 2.69.46.22:25410 Waiting to see if connection comes back online on its own. Connection back on its own. EMPI_Data Updated the expiring shields and MRNs to reflect the appropriate ones. Followed these notes Shields Duplicate Medrecs id'd in daily email Ensemble alert from HWVLBEENIEPR11: BP_multi_HIEPreProcessor_ADTORM QueueWaitAlert: Message Header Id '25246253184' queued for config item 'BP_multi_HIEPreProcessor_ADTORM' with priority 'Async' has been queued for more than 300 seconds First, The queue in both "BP_multi_HIEPreProcessor_ADTORM" and "To_Oracle_DDS_HIE" was caused by message id "'25246253184' ". The Oracle connection wasn't down, it was just encountering an error. I turned off both components, then aborted the message in both of their queues. After that, I turned them back online and the queues are now down. 2022-11-14 09:39:40.759 time stamp of the message causing the issue. Will re-try to send message, the message error was an XML message. BP_multi = 25246253111 To_Oracle = 25246253111 Event log showed ERROR <Ens>ErrBPTerminated: Terminating BP BP_multi_HIEPreProcessor_ADTORM # due to error: ERROR <Ens>ErrException: <INVALID OREF>zS8+8 ^BEIE.BPL.BPLmultiORMToHIEPreProcessor.Thread1.1 -- logged as '-' number - @' set context.SqlRS = tResponse.ResultSet' > ERROR <Ens>ErrException: <INVALID OREF>zS8+8 ^BEIE.BPL.BPLmultiORMToHIEPreProcessor.Thread1.1 -- logged as '-' number - @' set context.SqlRS = tResponse.ResultSet' Resent messages and everything was processed and queue has been cleared. QueueWaitAlert: Message Header Id '25249871975' queued for config item 'BP_CIS_multi_ADT_Merge' with priority 'Async' has been queued for more than 600 seconds Session ID was the issue 25249871902 Make sure to abort all the messages for this patient. Error reads: > ERROR <Ens>ErrGeneral: Disabling on Message body 8@EnsLib.HL7.Message / 8480214351 because Status 'ERROR #Error: Unknown status code: <UserErrors>Error (Unable to insert into MRG_TABLE call.)' matched ReplyCodeAction 1 : 'E#Error=D' resulting in Action code D Side note on dealing with the event log and message viewer It’s okay that only some of them show up We still had to abort all of them because we don’t want to send the messages out of order. If one message has an error, we have to abort all the related messages Reaching out to Prasad to figure out how to fix and resend the message. EMAIL/PAGER : daily file COMPASS_PA_A_YYYYMMDD.DAT has not been created since Oct 30th.   Why? I reached out to Julie C to figure out if she had known about this issue, she got back to me and I forwarded the email to her and then she got ahold of Amit. Ensemble alert from HWVLBEENIEPR11: To_Xealth_Multi / QueueWaitAlert: Message Header Id '25259788373' queued for config item 'To_Xealth_Multi' with priority 'Async' has been queued for more than 600 seconds Usually goes out around 3:30 PM PST and comes back around then. Wait 20-30 mins on alert. Connection usually comes back on. 11/15/2022 Ensemble alert from ROUTERLIVE1: To_WNEC_ORU_BRL_BHRAD QueueWaitAlert: Message Header Id '1634071051' queued for config item 'To_WNEC_ORU_BRL_BHRAD' with priority 'Async' has been queued for more than 600 seconds ERROR <Ens>ErrOutConnectExpired: TCP Connect timeout period (5) expired for 209.208.103.92:2315. Waiting to see if the connection comes back online by itself. Server hadn’t come on since 9AM EST, contacting support@mailchs.com The phone number given does not give access to her and reaches a help desk for the university. #InterfaceUrgent E-Mail Generated Request for: #InterfaceUrgent See Additional comments for full e-mail request. Cache is down on smslpvixpipr01 Reach out to Vitaliy or Amit immediately. Got contact back from Vitaliy and told me to assign the ticket to him. Ensemble alert from HWVLBEENIEPR11: BP_multi_HIEPreProcessor_ADTORM First, The queue in both "BP_multi_HIEPreProcessor_ADTORM" and "To_Oracle_DDS_HIE" was caused by message id "' 25273986343' ". The Oracle connection wasn't down, it was just encountering an error. I turned off both components, then aborted the message in both of their queues. After that, I turned them back online and the queues are now down. I went to the event log to find out the issue with the message. This is an issue with the DOB PID 7. Here is the message as is: Here is what the DOB should look like 20221111 Resubmitted new message to head of the queue. Sudha notes: 11/16/22 INC2988388, INC2988386 : Work Note: No Corp MNR found. Resent the message with active MRN. MDM Alert at 9.27: Work note : Looked at message, and address looks wired. So deleted the message and resent. INC2988923: No Hosp Service records Found. Work Note: So closed the ticket. Description works as designed. Got an email from  BP_Shields_multi_ADTORMORU saying DOB mismatch. Work Note: in email we have shields MRN so I search with Name in hnacombine  and in EDM … sent  email to shields team too check which is active MRN.(I see 2 MRN’s with same name and DOB.) waiting for them to respond. INC2989108: Work Note: No Corp MNR found. Resent the message with active MRN. Got an email from  BP_Shields_multi_ADTORMORU saying Sex mismatch Work note: Sent an email to Shields team to see which is correct gender. In our side it is male and in message it is female. waiting for them to respond. To_ChangeHealthcare_ORU_BRL_BHRAD with priority 'Async' has been queued for more than 600 seconds Work Note: connection is back and queue is clear. To_Xealth_Multi with priority 'Async' has been queued for more than 600 seconds Work Note: connection is back and queue is clear. 11/17/22 Deployment is going in BEENIE Nursing…and all the Processes came down had to jump into call and Amit said to start all processes manually. These are process that stopped. BP_CISLabORMORU_Internal BP_Sunquest_HWA_ORM, BP_SQCoPath_BRL_ORMORU, BP_multi_BRLExchange_ORU, BP_multi_BRLExchange_ORU, BP_Sunquest_HWA_ORM, BP_CIS_MDOC_HIE_ORU, BP_multi_XSOLIS_ORU_Lab, BP_multi_BRLExchange_ORU, BP_SQCoPath_BRL_ORMORU, BP_multi_AtlasSunquest_ORMORU, BP_multi_BayCare_ORU, BP_SunquestORMORU_Sunquest_ADT BP_Sunquest_TheraDoc_ORMORU, BP_Sunquest_TheraDoc_ORMORU, BP_multi_XSOLIS_ORU_Lab, BP_SMSPIDX_NursingCompass_ADT, BP_multi_AtlasSunquest_ORMORU, BP_multi_XSOLIS_ORU_Lab, BP_SunquestORMORU_Sunquest_ADT, BP_SunquestORMORU_Sunquest_ADT, To_NursingCompass_ADT, BP_SunquestCOPATH_Allscripts_ORU, BP_SMSPIDX_NursingCompass_ADT, BP_SunquestCOPATH_Allscripts_ORU INC2989757: BP_CIS_multi_ADT_Merge QueueWaitAlert: Message Header Id '25319439494' queued for config item      'BP_CIS_multi_ADT_Merge' with priority 'Async' has been queued for more than 600 seconds (Host is disabled) Work note: Aborted the message which is down and resent it by updating the message. INC2990363: INC2990360: Ensemble alert from HWVLBEENIEPR11: To_AIS_ADTSIU Connection is back and queue is clear. INC2990247: Ensemble alert from HWVLBEENIEPR11: BP_HCHB_multi_ADT Work Note: No active corp MRN. Resent with active Corp MRN. INC2989821, INC2989823, INC2989757:- -- Ensemble alert from HWVLBEENIEPR11: BP_CIS_multi_ADT_Merge: Aborted the message and In message there is expired SMRN fields and corrected and  Resent it INC2990025:-   INC2990022:-        BP_multi_HIEPreProcessor_ADTORM There the DOB length is too long so fixed the DOB and resent it. INC2990009: BP_multi_HIEPreProcessor_ADTORM Work note: By mistake message was aborted so resent it. 11/18 INC2990625: Ensemble alert from ROUTERLIVE1: To_SPMA_ORU_BRL EMPI DATA extract: see one note. Email from Shields regarding patient Gender Mismatch from InterfaceTeam@baystatehealth.org Work Note: Send email to shields integration service, Ally,Wendy and cc to secondary, integration team inbox. Once they reply back we have to forward that to duplicate medical records team. They will fix it. INC2991067: BP_SMSADT_Internal_1 ERROR <Ens>ErrBPTerminated: Terminating BP BP_SMSADT_Internal_1 # due to error: ERROR <Ens>ErrGeneral: Suspending Message body 10@EnsLib.HL7.Message / 8514810301 because Status 'ERROR #Skip: Unknown status code: <UserErrors>Skip (ERROR High Level Validation: Multiple Hospital Service entries found! Stopping BP)' matched ReplyCodeAction 2 : 'E#Skip=S' resulting in Action code S > ERROR <Ens>ErrGeneral: Suspending Message body 10@EnsLib.HL7.Message / 8514810301 because Status 'ERROR #Skip: Unknown status code: <UserErrors>Skip (ERROR High Level Validation: Multiple Hospital Service entries found! Stopping BP)' matched ReplyCodeAction 2 : 'E#Skip=S' resulting in Action code S Work Note : Nothing to work close as working as designed. INC2991066--- BP_SMSADT_Internal_1 ERROR High Level Validation: Multiple Hospital Service entries found Work note : Working as designed. INC2991083, INC2991078-- To_CIS_MDM_Rad: Work note: connection issue. EXCHANGE Order Processing Error( we will get email) There is in one note so I saw that message and forwarded to LIS Team. 11/19/2022 To_ONCORE_ADT, To_Keriton_ORM, To_Keriton_ADT Work note:Connection issue. INC2991975 : BP_EPointCIS_DFT_SMS_Charges INFO^CIS Charge did not process^Unable to drop charge for Accession number  #00000MR20220042141, due to missing final result. Work Note: Followed the instructions to update the Result Status and result date with correct date by checking in radorderviewer for this accession number and resent the charge. Still failed to process as account number in EMR_ORDER_TABLE is more than 10 digit number and matched with cerner. But when checking the query, program is using only 10 digit and failed the query. Assigning this to Prasad K for further review.  Account number in EMR_ORDER_TABLE - SMRI644268820221115 Account number using in query - SMRI6442688  Account number in CIS - SMRI644268820221115 Assigned to prasad. 11/21/22 INC2990783- PatientKeeper not crossing over to SMS/Invision Looks like this is similar to INC2987318. Charges are in Message Viewer and showing it writing to a file. But when I checked the archive files, there is no entry for the accounts.               Charges between 7AM till midnight are missing. Assigning this to Prasad K for further review. INC2993624-- BP_HIE_EMR_Internal Queued up messages. Work Note: BP_HIE_EMR_Internal is in green and To_oracle_DDS_HIE_EMR is purple. So went to To_oracle_DDS_HIE_EMR and stopped and then BP_HIE_EMR_Internal  stopped that also. Then delete the first message from To_oracle_DDS_HIE_EMR and first message from BP_HIE_EMR_Internal and started oracl and BP ….Then the queue should be clear. Then go to messages and see what is wrong. In this message Address column is having extra thing not sure about this. Checking with prasad k. MDM Alert: In email. [ BSOG-112116 ] is not Active Took help of Sam and finished. INC2993815: BP_EPointCIS_DFT_SMS_Charges INFO^CIS Charge did not process^Unable to drop charge for Accession number  #00000MR20220042141, due to missing final result. The same Accession Number Ticket is there on 19th so assignig it to prasad. FW: INC2993597 Got a email regarding this INC  as I believe they need to put the missing MRNs in CIS?? Work Note: So went to that process and opened that record and sent an A31 record with all MRN’s So all MRNs are created in Cerner.  Update on this INC That is given in email. INC2993597-- Sent an A31 to add the missing MRN's in CIS. Record is ready for merge process. 11/23/22 INC2995181 CIS chart showing with same name Contacted Mike Barnhardt, he said reach to Prasad K. Reached out Prasad. 1617916 this patient is showing a separate active CIS but in our EDM this is showing merged into 7317390. INC2996284 Ensemble alert from HWVLBEENIEPR11: BP_HCHB_multi_ADT No Active CORP MRN found with Inbound PID-4:2360570 Found the Proper MRN and changed to the correct one. INC2996304 Ensemble alert from HWVLBEENIEPR11: BP_multi_HIEPreProcessor_ADTORM Message had DOB with time included, changed the DOB to not include the time. Resent message. INC299637 Ensemble alert from HWVLBEENIEPR11: BP_CIS_multi_ADT_Merge Found the patient who was causing the buildup 25440587153 It was a patient who has been giving issues it was 100+ADT_44 Messages. Aborted those. Now to resend with the correct SMRI INC2996430 Ensemble alert from HWVLBEENIEPR11: BP_HCHB_multi_ADT Expired MRN Updated the MRN to the active one. INC2996484 Ensemble alert from HWVLBEENIEPR11: To_Xealth_Multi Stop the operation and abort the message and start Did not resend because in the error message it said to not resend INC2996611 Ensemble alert from HWVLBEENIEPR11: BP_multi_HIEPreProcessor_ADTORM DOB included time in the message. Made the fix and resent the message.""",

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

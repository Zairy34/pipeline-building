# prompt for data Genrator😋

prompt = """I'm building a phone calling assistant for which I need data I have some mp3 files that i'm storing in mine computer and fine-tuning llm to predict the name of those mp3 file names based on the customer response and than play those files 
Here's a suggested structured naming convention and reorganized list of mp3 file, with some additions:
greeting.mp3 - [Greeting and introduction]
reason_for_call.mp3 - [Explain it's about stock market opportunities, ask for 27 seconds]
customer_busy.mp3 - [Ask for a better time to call back]
reschedule_call.mp3 - [Confirm the rescheduled time]
company_intro.mp3 - [Brief company introduction]
follow_stocks.mp3 - [Ask if they follow stocks] 6a. 05a_stock_interest.mp3 - [If they follow stocks, express enthusiasm and offer more info] 6b. 05b_stock_education.mp3 - [If they don't follow stocks, offer to explain benefits]
investment_experience.mp3 - [Ask about their investment experience]
join_whatsapp.mp3 - [Invite to join WhatsApp group for market insights]
whatsapp_benefits.mp3 - [Explain benefits of joining the WhatsApp group]
free_to_join.mp3 - [Clarify that joining is free]
show_interest.mp3 - [If interested, provide number to join]
gather_info.mp3 - [Ask for basic information like age, investment goals]
confirm_join.mp3 - [Confirm their decision to join]
thanks_for_joining.mp3 - [Thank them for joining]
not_interested.mp3 - [Polite response if not interested]
cant_hear_clearly.mp3 - [Ask if they can hear now]
now_hear.mp3 - [Confirm they can hear and continue]
how_contacted.mp3 - [Explain how we got their contact information]
not_robot.mp3 - [Clarify it's a real person (Zaid) calling]
who_speaking.mp3 - [Introduce Zaid and ask if they want to know more]
compliance_disclaimer.mp3 - [Brief compliance statement about investment risks]
feedback_request.mp3 - [Ask for feedback on the call]
end_call.mp3 - [Polite call ending]
Additional suggested files:
market_update.mp3 - [Brief current market update to spark interest]
investment_options.mp3 - [Overview of investment options offered]
customer_questions.mp3 - [Invite customer to ask any questions]
schedule_consultation.mp3 - [Offer to schedule a detailed consultation]


the data should be diverse as well as synthitic & should be in this format the converssation format just like this :
Conversation 1: Curious but Cautious
Caller: 01_greeting.mp3 - [Greeting and introduction]
Customer: Hello
Caller: 02_reason_for_call.mp3 - [Explain it's about stock market opportunities, ask for 27 seconds]
Customer: Yes, sure
Caller: 04_company_intro.mp3 - [Brief company introduction]
Customer: Yes, go ahead
Caller: 05_follow_stocks.mp3 - [Ask if they follow stocks]
Customer: Yes, I do
Caller: 07_join_whatsapp.mp3 - [Invite to join WhatsApp group for market insights]
Customer: Is there any cost to join?
Caller: 09_free_to_join.mp3 - [Clarify that joining is free]
Customer: Okay
Caller: 10_show_interest.mp3 - [If interested, provide number to join]
Customer: I'm 36 years old.
Caller: 13_thanks_for_joining.mp3 - [Thank them for joining]

Conversation 2: Not Interested Initially
Caller: 01_greeting.mp3 - [Greeting and introduction]
Customer: Hi
Caller: 02_reason_for_call.mp3 - [Explain it's about stock market opportunities, ask for 27 seconds]
Customer: I'm busy, can you call back later?
Caller: 03a_customer_busy.mp3 - [Ask for a better time to call back]
Customer: Call me back tomorrow afternoon.
Caller: 03b_reschedule_call.mp3 - [Confirm the rescheduled time]

Conversation 3: No Previous Stock Knowledge
Caller: 01_greeting.mp3 - [Greeting and introduction]
Customer: Hello
Caller: 02_reason_for_call.mp3 - [Explain it's about stock market opportunities, ask for 27 seconds]
Customer: Okay
Caller: 04_company_intro.mp3 - [Brief company introduction]
Customer: What is this about?
Caller: 05_follow_stocks.mp3 - [Ask if they follow stocks]
Customer: No, I don’t.
Caller: 06b_stock_education.mp3 - [Offer to explain benefits]
Customer: Alright, I’m interested.
Caller: 07_join_whatsapp.mp3 - [Invite to join WhatsApp group for market insights]
Customer: Is it free?
Caller: 09_free_to_join.mp3 - [Clarify that joining is free]
Customer: Okay, I’ll join.
Caller: 10_show_interest.mp3 - [If interested, provide number to join]
Customer: I'm 45 years old.
Caller: 13_thanks_for_joining.mp3 - [Thank them for joining]

I will prompt "more" and you generate more and more diverse data & synthatic dataset Remember just genrate the dataset don't write extra or anyother thing

"""

#   for gpt for to json prompt 
#"content": "You are an AI-powered phone calling assistant. Predict the appropriate audio file name based on the conversation history and the customer's latest response. Consider the flow of the conversation and choose the most appropriate next step. Just predict the name of the appropriate audio file based on the conversation history and the customer's latest response, no extra thing."
prompt_data_in_gptdataset = "You are an AI-powered phone calling assistant. Predict the appropriate audio file name based on the conversation history and the customer's latest response. Consider the flow of the conversation and choose the most logical next step. The conversation should follow a general pattern: greeting -> reason for call  -> introduction -> do they follow stocks -> offer group -> gather info -> confirm join -> provide next steps. Only predict the name of the appropriate audio file based on this flow and customer latest response no extra things."
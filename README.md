# Customized-LLM-Chatbot-for-a-University-Website-using-Vertex-AI-Agent-Builder-Dialogflow
A Customized LLM Chatbot for a University Website Trained on my Own Data Using Google Vertex AI Agent Builder

## Overview

I created a custom-trained LLM Chatbot using the Google Vertex AI Agent Builder. LLMs are Large Language Models - a type of Machine Learning model that is trained on massive amounts of text data, which allows them to output text, performing a variety of tasks, including generating emails, code, letters, conversational responses, understanding language and its semantic and contextual meaning, and summarising information, for example receiving a large piece of text and condensing it into a short summary.

Many companies like Google and OpenAI have trained such language agents on massive amounts of data, making them incredibly versatile tools, capable of conversing with the user and performing some of the tasks mentioned earlier. However, they can struggle with understanding specific domains or tasks they have not been fed training data on. This can be a hindrance if you’re trying to build a chatbot tailored to your business needs.

## Building a Custom Chatbot

By training a Foundational LLM model on your own data, you can ensure it understands the specific terminology and concepts relevant to your domain. This can significantly improve the accuracy and effectiveness of your chatbot.

### Vertex AI Agent Builder

Vertex AI Agent Builder is a user-friendly platform that allows you to build and deploy custom LLMs for chatbots. It offers a no-code interface, making it accessible even for those without extensive programming experience. 

### Building a Generativ ChatBot with Vertex AI Agent Builder

  1- Navigate to Vertex AI Agent Builder from Cloud Console and Activate API. Credits will be added to your billing Accounts once API is activated.
  2- Create an App: Within the Vertex AI Agent Builder interface, you’ll first create a new application > Chat Application.
  3- Build a Datastore: This is where you can upload your custom data, like documents, FAQs, product descriptions, or any other relevant information you want your chatbot to be familiar with. I uploaded html pages from the LUMS website and other pdf documents related to information about the admissions process.
  4- Connect Datastore to App: Link the datastore to the chatbot application created earlier.
  5- Configure Generative AI Model with Conversational Agent: Vertex AI integrates with Conversational Agent, a conversational AI platform from Google
  6- Test and Integrate: Once I built my chatbot, I tested it within the Vertex AI interface to see how it responds to different queries. Then I integrated the chatbot into a webpage.

<img width="257" height="420" alt="Screenshot 2025-06-26 084433" src="https://github.com/user-attachments/assets/c27dae01-1d79-4ce5-a7ad-4189af2e1ec4" />

  


# JobYaari AI Chatbot - Assignment 2

## Project Overview
AI-powered chatbot for JobYaari website that intelligently responds to government job queries across Engineering, Science, Commerce, and Education categories.

## Features
✅ Real-time job data extraction from JobYaari.com  
✅ AI-powered conversational interface using LangChain  
✅ Category-specific job search and filtering  
✅ Experience and qualification-based recommendations  
✅ Responsive web interface  

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Set up your OpenAI API key in `.env` file
3. Run data extraction: `python data_extraction/scraper.py`
4. Start chatbot: `python chatbot_app/app.py`
5. Open browser: `http://localhost:5000`

## Project Structure
- `data_extraction/` - Web scraping module
- `chatbot_app/` - Main Flask application
- `documentation/` - Project documentation and media

## Assignment Requirements Met
- ✅ Web scraping from JobYaari.com
- ✅ Knowledge base creation
- ✅ AI chatbot with LangChain
- ✅ Category-wise job information
- ✅ Live web interface

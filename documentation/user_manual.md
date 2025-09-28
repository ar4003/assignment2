# JobYaari AI Chatbot - User Manual

## 🎯 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Internet connection
- Chrome browser (for data extraction)

### Installation Steps

1. **Download and Extract Project**
cd jobyaari-chatbot

2. **Install Python Dependencies**
pip install -r requirements.txt


3. **Set Up Environment Variables**
- Create `.env` file in project root
- Add your OpenAI API key:
  ```
  OPENAI_API_KEY=your_api_key_here
  FLASK_SECRET_KEY=your_secret_key
  ```

4. **Run Data Extraction**
python data_extraction/scraper.py

5. **Start the Chatbot**
python chatbot_app/app.py


6. **Access the Application**
- Open browser and go to: `http://localhost:5000`

## 💬 How to Use the Chatbot

### Supported Question Types

1. **Category-Specific Queries**
- "Show me Engineering jobs"
- "What are the latest Science notifications?"
- "Commerce job opportunities"
- "Education sector vacancies"

2. **Experience-Based Searches**
- "Jobs for freshers"
- "Positions requiring 2 years experience"
- "Senior level opportunities"

3. **Qualification Queries**
- "B.Tech jobs in government"
- "What qualifications needed for XYZ post?"
- "Graduate level positions"

4. **Salary and Benefits**
- "High salary government jobs"
- "Jobs with salary above 50000"
- "Pay scale information"

5. **Organization-Specific**
- "ISRO job openings"
- "Railway recruitment notifications"
- "Bank job opportunities"

### Sample Conversations

**User**: "What are the latest notifications in Engineering?"
**AI**: "Here are the latest Engineering job notifications:

1. **Graduate Engineer Trainee** at NUMALIGARH REFINERY LIMITED
- Salary: ₹50,000 - ₹1,60,000
- Experience: Fresher
- Qualification: B.E/B.Tech
- Specializations: Civil, Computer Science, Electrical, Mechanical...

2. **Junior Engineer** at Kerala PSC
- Salary: ₹9,190 - ₹15,780
- Experience: Fresher
- Qualification: B.E/B.Tech (Civil)..."

## 🛠️ Troubleshooting Guide

### Common Issues and Solutions

1. **"Chatbot not available" Error**
- **Cause**: Missing or invalid OpenAI API key
- **Solution**: Check your `.env` file and ensure valid API key

2. **"Knowledge base not found" Error**
- **Cause**: Data extraction not completed
- **Solution**: Run `python data_extraction/scraper.py` first

3. **Slow Response Times**
- **Cause**: Large dataset or API rate limits
- **Solution**: Reduce query complexity or wait between requests

4. **Browser Automation Fails**
- **Cause**: Chrome driver issues or network problems
- **Solution**: Update Chrome browser and check internet connection

### Error Messages and Meanings

| Error Message | Meaning | Solution |
|---------------|---------|----------|
| "ChromeDriver not found" | Selenium can't find Chrome driver | Install Chrome browser |
| "OpenAI API limit exceeded" | Too many API requests | Wait or upgrade API plan |
| "Connection timeout" | Network connectivity issue | Check internet connection |
| "Invalid response format" | Unexpected API response | Retry the request |

## 📊 Data Categories and Coverage

### Job Categories
1. **Engineering** (500+ jobs)
- Civil Engineering
- Computer Science
- Electrical Engineering
- Mechanical Engineering
- Chemical Engineering

2. **Science** (200+ jobs)
- Research positions
- Laboratory roles
- Technical positions
- Academic roles

3. **Commerce** (300+ jobs)
- Accounting positions
- Finance roles
- Banking jobs
- Management positions

4. **Education** (250+ jobs)
- Teaching positions
- Administrative roles
- Academic positions
- Training roles

### Data Fields Available
- Job Title
- Organization Name
- Salary Range
- Experience Requirements
- Educational Qualifications
- Age Limits
- Number of Vacancies
- Location/State
- Application Deadlines

## 🔧 Advanced Usage

### Custom Queries
The AI chatbot can handle complex, multi-part questions:

- "Show me Engineering jobs in ISRO with B.Tech qualification and salary above 40000"
- "What are the age limits for Commerce jobs in banking sector?"
- "Compare qualification requirements between Science and Engineering positions"

### Best Practices for Queries
1. **Be Specific**: Include category, experience level, or organization
2. **Use Keywords**: Mention specific qualifications or salary ranges
3. **Ask Follow-ups**: Build on previous questions for more detailed information
4. **Check Sources**: Review the job sources provided with each response

## 📱 Mobile Usage
The chatbot interface is fully responsive and works on:
- Smartphones (iOS/Android)
- Tablets
- Desktop computers
- All modern web browsers

## 🔄 Data Updates
- Job data is extracted from live JobYaari website
- Run data extraction script weekly for latest notifications
- Knowledge base automatically updates with new data
- No manual intervention required for updates

## 📞 Support and Feedback
For technical issues or feature requests:
1. Check this user manual first
2. Review error messages and troubleshooting guide
3. Ensure all prerequisites are met
4. Verify API key and internet connectivity

## 🎓 Tips for Best Results
1. **Start with category-specific questions** for better results
2. **Use natural language** - the AI understands conversational queries
3. **Ask for clarification** if responses are too general
4. **Explore different phrasings** if initial results aren't satisfactory
5. **Use the quick question buttons** for common queries

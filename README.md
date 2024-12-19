# Automated Web Data Extraction with Selenium  

This project demonstrates how to use **Selenium**, **Python**, and **regex** to automate the extraction of data from a web page. Specifically, it retrieves the description of a YouTube video and extracts timestamps in the format `mm:ss`. The project was created as part of a technical assessment.  

## Features  
- **Web Automation**: Uses Selenium to retrieve video descriptions from YouTube.  
- **Timestamp Extraction**: Employs regex to extract all timestamps (in `mm:ss` format) from the description.  
- **Output Handling**: Prints the video description and extracted timestamps in a clean format within Google Colab.  
- **Data Storage**: Saves the YouTube URL and extracted timestamps to a text file for reference.  

## Requirements  
- **Python 3.7 or above**  
- **Google Chrome** and **Chromedriver**  
- **Google Colab** environment (or local machine with Selenium setup)  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```  

2. Install dependencies:  
   ```bash
   pip install selenium
   ```  

3. Set up Chromedriver:  
   - Download Chromedriver from [here](https://sites.google.com/chromium.org/driver/) based on your Chrome version.  
   - Place the Chromedriver executable in a known path and update the script accordingly.  

## Usage  
1. Open the `python_web_scraping_colab.ipynb` notebook in Google Colab.  
2. Follow these steps:  
   - Install Selenium and set up Chromedriver within Colab.  
   - Run the script to extract the description and timestamps.  
3. Results:  
   - The extracted description and timestamps are printed in an output cell.  
   - A `.txt` file is generated containing the YouTube URL and timestamps.  

## Example Output  
**Extracted Description:**  
```
This is an example description from a YouTube video.  
```  

**Extracted Timestamps:**  
```
['01:23', '02:45', '05:10']  
```  

**Text File Format:**  
```
URL: https://youtu.be/iTmlw3vQPSs  
Timestamps: 01:23, 02:45, 05:10  
```  

## Challenges  
- Setting up Selenium in Google Colab due to WebDriver initialization issues.  
- Creating an optimized regex pattern to accurately extract timestamps.  

## Improvements  
Future improvements could include:  
- Adding support for more timestamp formats.  
- Handling dynamic pages with JavaScript rendering.  
- Extending functionality to extract additional metadata.  

## License  
This project is licensed under the MIT License. See the `LICENSE` file for details.  

## Contact  
Feel free to reach out with any questions or feedback:  
- **Email**: vinayvasantham7@gmail.com  
- **GitHub**: [vinayvasantham](https://github.com/vinayvasantham)  

Happy coding! 🚀

# Webtoon Downloader
A crawler that allows you to download cartoons  
from Naver Webtoon and Marumaru by specifying the section you want.
  
# Select a cartoon
Search [titleID] from the HTML source of  
the specific episode of the cartoon you want to download.  
Then, assign to the variable [titleID] in NaverWebtoonDownloader.py
  
# Specify a section
Most of the cartoons are divided into chapters, such as Chapter 1 - 000, and Chapter 2 - 000.  
The remote control provided by Naver Webtoon does not care about the chapter and tells the number of episodes.  
Adjust the variable [no_MAX] of NaverWebtoonDownloader.py and the range of the for-statement  
based on the information from the remote control.
  
## Notes
2020-08-30 : Branch creation/development completed for Marumaru
  
# etc.
I left it because I used Selenium at the beginning of writing the code.  
In practice, it doesn't make much sense because there is no asynchronous data being received.

#####################################################################################################################
#                                                                                                                   #
# User should be able to enter a prompt and system will search for corresponding URL                                #
# GPT will search correct URL, open a browser and take a screenshot out of it.                                      #
# Based on the screenshot, we'll use vision APIs to understand the screenshot, extract content out of it and        #
# give the result back to user by extracting text out of it.                                                        #
#                                                                                                                   #
# We'll use puppeteer in node.js to open URL and take screenshot.                                                   #    
# We'll use GPT4 to get the URLs                                                                                    #
# We'll use GPT4-vision API to understand the images.                                                               #
#                                                                                                                   #
# We'll have user give option to use GPT or Gemini                                                                  #
#                                                                                                                   #
# Inspiration: https://www.youtube.com/watch?v=VeQR17k7fiU - Easy Web Scraping                                      #                                                                             #
#####################################################################################################################                                                         


# Local Deployment Guide

1. Build the Docker image:
   `docker build -t student-productivity-api .`
2. Run the container:
   `docker run -p 5000:5000 student-productivity-api`
3. Test the endpoint:
   `python test.py`

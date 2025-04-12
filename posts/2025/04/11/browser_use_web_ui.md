---
title: Try Browser Use /web-ui to control your browser automation
date: 2025-04-08
layout: layout/post.html
tags:
  - posts
  - gRPC
  - SSL
  - troubleshooting
  - Browser Use
---

Have you explored [Browser Use](https://github.com/browser-use/browser-use) yet? It is one of the most exciting projects I have recently worked with, leveraging an LLM (Large Language Model). I used its GUI, [web-ui](https://github.com/browser-use/web-ui), which is straightforward to set up by following the project documentation.

While the project worked seamlessly for me initially, I encountered an SSL issue while connected to a VPN. As someone who does not use Python daily, I was unfamiliar with the error and spent several hours investigating the problem. Eventually, I discovered that the issue was related to the gRPC Python module. For reference, you can find more details in [gRPC Issue #27727](https://github.com/grpc/grpc/issues/27727).

To fix the problem, 
- Export certificate from Browser (Chrome)
- Import `*.pem` to ceritificate store in Python
- Set the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to point to the correct certificate file. Here is the configuration I used for `.env` browser-use:

`

GRPC_DEFAULT_SSL_ROOTS_FILE_PATH="C:\\Users\\ssing\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\certifi\\cacert.pem"


`
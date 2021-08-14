# Desmos-Offline
Desmos.com's Graphing Calculator for Offline Use

## About
This is a stripped down version of Desmos' Graphing Calculator you can use offline. However, because you are hosting this yourself, authentication APIs will fail (calling you instead of Desmos), you can not sign in with your account and save your project. So, this is meant for quick calculations or quick modeling.

## How to Use
1. Download the repository
1. Open a terminal
1. `cd` into the folder where you downloaded it
1. In the folder, type `python -m http.server --directory www.desmos.com`
1. Open [http://localhost:8000/calculator.html](http://localhost:8000/calculator.html). It should load and you can use it like normal.

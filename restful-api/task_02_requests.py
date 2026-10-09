#!/usr/bin/python3
"""
Module to fetch posts from JSONPlaceholder using requests
and process/save them into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves them into a CSV file named posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)

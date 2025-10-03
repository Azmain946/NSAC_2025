# NSAC 2025

## WebApp

### Follow the link --> https://nasa-space-app-2025.vercel.app/

## Overview

This project is a web application designed for the NASA Space Apps Challenge 2025. It serves as a platform for exploring and analyzing NASA's vast collection of scientific and technical publications. The application provides a user-friendly interface to search, visualize, and interact with the knowledge graph of publications, authors, and research categories.

## Data Source

We have collected our data mainly from **A list of 608 full-text open-access Space Biology publications** from NSAC website. We have also collected data from **National Library of Medicine (NIH)**, **Nature.com** etc.

## About Our Project

Our project **SpaceBio Explorer** is a publication summarization tool. It offers interactive search, filters, and the ability to browse publications by year, category, and subcategory. Each publication tab includes the title, authors, and keywords in the heading section. Abstracts and summaries are provided based on the user type (Scientist, Investor, or Mission Architect).

There is also an AI-generated podcast section where two speakers discuss the publication. A knowledge graph is included, which can be zoomed in and out. Scientific Progress, Knowledge Gaps, and Consensus/Disagreement are presented as buttons with floating cards.

For instant insights, users can access the AI-generated FAQ section. Quick Links allow direct access to the raw publication. Additionally, an AI-powered chatbot is available for asking custom questions about the publication.

## Demo

![alt text] (https://github.com/Azmain946/NSAC_2025/blob/main/Screenshot%202025-10-03%20162842.png?raw=true)

## Architecture

The project is divided into two main parts:

-   **Frontend:** A React application built with Vite and written in TypeScript. It uses Shadcn UI for components and Tailwind CSS for styling.
-   **Backend:** A Python application built with FastAPI. It uses a PostgreSQL database and SQLAlchemy for ORM. It also uses LangChain for...

## Features

-   **Search:** Search for publications by keyword, author, or category.
-   **Knowledge Graph:** Visualize the relationships between publications, authors, and research categories in an interactive graph.
-   **Q&A:** Ask questions about the publications and get answers from a language model.
-   **Analytics:** View analytics and statistics about the publications and authors.
-   **Publications:** View a list of publications and their details.
-   **Categories:** Browse publications by research category.

## Frameworks and Libraries (Technical Stacks)

### Frontend

-   **React:** A JavaScript library for building user interfaces.
-   **Vite:** A build tool that aims to provide a faster and leaner development experience for modern web projects.
-   **TypeScript:** A typed superset of JavaScript that compiles to plain JavaScript.
-   **Shadcn UI:** A collection of re-usable components for React.
-   **Tailwind CSS:** A utility-first CSS framework for rapidly building custom designs.
-   **React Router:** A standard library for routing in React.
-   **Axios:** A promise-based HTTP client for the browser and Node.js.

### Backend

-   **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
-   **SQLAlchemy:** The Python SQL toolkit and Object Relational Mapper.
-   **PostgreSQL:** A powerful, open source object-relational database system.
-   **LangChain:** A framework for developing applications powered by language models.
-   **Uvicorn:** An ASGI server implementation, for use with FastAPI.

## Getting Started

### Prerequisites

-   **Node.js:** v22.x or later
-   **npm:** v10.x or later
-   **Python:** 3.10 or later
-   **pip:** 23.x or later

### Installation

**Frontend:**

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install dependencies: `npm install`
3.  Start the development server: `npm run dev`

**Backend:**

1.  Navigate to the `backend` directory: `cd backend`
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment:
    -   On Windows: `venv\Scripts\activate`
    -   On macOS/Linux: `source venv/bin/activate`
4.  Install dependencies: `pip install -r requirements.txt`
5.  Create a `.env` file from the `.env.example` and update the environment variables.
6.  Run the application: `uvicorn app.main:app --reload`

## Usage

Open your browser and navigate to the address provided by the frontend development server (usually `http://localhost:5173`).

## Contributing

Contributions are welcome! Please follow the existing code style and submit a pull request.

# NSAC 2025

## WebApp

### Follow the link --> https://nasa-space-app-2025.vercel.app/

## Overview

This project is a web application designed for the NASA Space Apps Challenge 2025. It serves as a platform for exploring and analyzing NASA's vast collection of scientific and technical publications. The application provides a user-friendly interface to search, visualize, and interact with the knowledge graph of publications, authors, and research categories.

## Data Source

We have collected our data mainly from **A list of 608 full-text open-access Space Biology publications** from NSAC website. We have also collected data from **National Library of Medicine (NIH)**, **Nature.com** etc.

## About Our Project

Our project **SpaceBio Explorer** is a publication summarization tool. It offers interactive search, filters, and the ability to browse publications by year, category, and subcategory. Each publication tab includes the *title*, *authors*, and *keywords* in the heading section. *Abstract* and *summaries* are provided based on the user type (Scientist, Investor, or Mission Architect).

There is also an AI-generated *podcast* section where two speakers discuss the publication. A *knowledge graph* is included, which can be zoomed in and out. *Scientific Progress, Knowledge Gaps, and Consensus/Disagreement* are presented as buttons with floating cards.

For instant insights, users can access the AI-generated *FAQ* section. *Quick Links* allow direct access to the raw publication. Additionally, an AI-powered *chatbot* is available for asking custom questions about the publication.

## Demo


![alt text](https://github.com/Azmain946/NSAC_2025/blob/main/Screenshot%202025-10-03%20162842.png?raw=true)


![alt text](https://github.com/Azmain946/NSAC_2025/blob/main/Screenshot%202025-10-03%20162907.png?raw=true)


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

### Impact and Use Cases

**Scientists** and **researchers** will use this tool to quickly digest complex biology publications, saving time while staying updated on the latest discoveries. **Mission architects** can explore biology-related insights crucial for designing safe and sustainable space missions. **Investors** benefit by identifying promising scientific directions and technologies with real-world or space applications. The interactive knowledge graph helps all users see connections between studies, gaps in research, and areas of consensus or disagreement.

For **NASA**, this tool matters because it accelerates understanding of space biology, a field essential for long-duration human spaceflight and planetary exploration. By providing instant summaries, FAQs, and even AI-driven podcasts, it reduces the barrier to accessing and interpreting dense research. Globally, it fosters collaboration by making space biology knowledge more accessible to scientists across disciplines. Ultimately, this contributes to advancing space science, healthcare, and technology for the benefit of humanity.

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

Open your browser and navigate to the address provided by the frontend development server (usually `http://localhost:3000`).

## Contributions

- Soab Mahmud: Built Backend
- Shahin Rana: Built Frontend
- Azmain Fieque: Designed UI 

Contributions are welcome! Please follow the existing code style and submit a pull request.

## Future Roadmap

SpaceBio Explorer is built with React on the frontend and FastAPI on the backend, making it modular and scalable. The current integration with LLM-based AI services demonstrates strong potential, but future iterations could move toward fine-tuning or developing custom AI models trained on domain-specific space biology literature. This would improve accuracy, context-awareness, and trustworthiness of summaries and recommendations.

For scalability, cloud deployment with containerization (Docker, Kubernetes) can handle increasing user demand from research institutions, universities, and space agencies worldwide. Improved user interaction features, such as personalized dashboards, collaboration tools, and citation management, could extend the platform’s utility. Integrating multimodal inputs—like visual data from experiments or astronaut health metrics—could open entirely new layers of insight.

Beyond the hackathon, SpaceBio Explorer has the potential to become a global research hub for biology in space, bridging scientists, investors, and mission planners with actionable knowledge that supports NASA’s missions and advances global science.

# Festiplan
## Project for subject - web design (II semestar)

This project has been created as pre-exam obligation for course *Web Design*. Detailed specification can be found in [Project Spesifications](https://github.com/MihajloMilojevic/FestiPlan-wdp/blob/master/materijali/WD%202024%20Specifikacija%20projekta.pdf). The purpose of this project was to create a frontend for a website with features listed below.

## Demo

You can try out a live demo of the project [here](https://festiplan.netlify.app/).

## Features

- **Browse Festival Organizers:** Look through a list of all registered festival organizers
- **Organizer's Details:** Look at organizers details and a list of all festivals organizers by them
- **Festival's Details:** Look at festivals details
- **Filtering:** Filter organizers list by name and filter festivals by name, type, transportation, price...
- **Searching:** Search for a text on a page
- **Users:** Allow users to register and login
- **Admin:** Allow admin (no roles on this project and this is accessible for everyone) to view, create, update and delete organizers, festivals and users  

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, React.js
- **Backend:** Firebase
- **Database:** Firebase Realtime Database

## Getting Started

To get started with the Festiplan project, follow these steps:

### Prerequisites

Before you begin, make sure you have the following installed on your local machine:

- Node.js: [Download and Install Node.js](https://nodejs.org/)
- npm: Typically comes with Node.js installation

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MihajloMilojevic/FestiPlan-wdp.git
```
2. Navigate to the project folder
```bash
cd festiplan-wdp
```
3. Install dependencies:
```bash
npm install
```

### Running the Application
Once you've installed the dependencies, you can start the development server by running:
```bash
npm start
```
This will launch the application locally. You can then access it in your web browser at http://localhost:3000.

### Building for Production
To build the application for production, run:
```bash
npm run build
```
This command will generate optimized production-ready files in the build directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
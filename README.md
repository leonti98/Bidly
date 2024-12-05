# Django Auction Project


This Django project is an auction platform that allows users to list items for 
bidding, place and manage bids, engage with other users through comments, and 
create personalized wishlists.

## Home page
![home](./screenshots/Screenshot%202024-12-05%20at%2012-27-32%20Auctions.png)
**view more screenshots at the end of the README**

## Features

- **User Authentication**: Users can register, log in, and log out to access their accounts.
- **Auction Lot Management**: Users can create new auction lots, view existing ones, and close lots when bidding concludes.
- **Dynamic Bidding System**: Users can place bids on active lots, with the highest bid price automatically updating every 10 seconds.
- **Category Organization**: Auction lots are organized into main and subcategories for easier browsing.
- **Interactive Comments**: Users can share their thoughts by leaving comments on auction lots.
- **Wishlist Feature**: Users can save their favorite lots by adding them to wishlist.
- **Seamless Pagination**: Lots are displayed with paginated navigation, ensuring an organized and user-friendly browsing experience across categories.

## Technologies Used

- **Python**: Backend development using Django.
- **Django**: Python web framework for building web applications.
- **Bootstrap 5**: Frontend styling and components.
- **SQLite**: Default database engine provided by Django.

## Installation

### Clone repository
```bash
git clone https://github.com/leonti98/Bidly
```
### Change directory
```bash
cd Bidly
```
### Intstall required packages
```bash
pip3 install -r requirements.txt
```
### Create database
```bash
python3 manage.py make migrations auctions
```
```bash
python3 manage.py migrate
```
### Run server
```bash
python3 manage.py runserver
```
### Access the website
Open your web browser and go to http://127.0.0.1:8000/

## Screenshots

### Lot detail view with comments and bid form.
![Lot detail](./screenshots/Screenshot%202024-12-05%20at%2012-28-53%20Auctions.png)

### Login required to bid on lots and leave comments.
![Login requirement](./screenshots/Screenshot%202024-12-05%20at%2012-27-54%20Auctions.png)

### Sub category view with paginated lots.
![sub category](./screenshots/Screenshot%202024-12-05%20at%2012-28-04%20Auctions.png)

### Main categories view.
![Main Categories](./screenshots/Screenshot%202024-12-05%20at%2012-31-00%20Auctions.png)
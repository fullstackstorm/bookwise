-- SQLite
SELECT books.name AS book_name, authors.name AS author_name, genres.name AS genre_name
FROM books
JOIN authors ON books.author_id = authors.id
JOIN genres ON books.genre_id = genres.id;

# Library-Management

1. SQL Query for Write a query to get all books that have never been borrowed:
SELECT 
    b.book_name AS "Book Name",
    b.author AS "Author"
FROM 
    Book b
LEFT JOIN 
    Issuance i ON b.book_id = i.book_id
WHERE 
    i.book_id IS NULL;




2.  Write a query that can list the outstanding books at any given point in time
SELECT 
    m.mem_name AS "Member Name",
    b.book_name AS "Book Name",
    i.issuance_date AS "Issuance Date",
    i.target_return_date AS "Target Return Date",
    b.book_publisher AS "Author"
FROM 
    Issuance i
JOIN 
    Member m ON i.mem_id = m.mem_id
JOIN 
    Book b ON i.book_id = b.book_id
WHERE 
    i.target_return_date >= CURRENT_DATE;




3.  Write a query to extract the top 10 most borrowed books 
SELECT 
    b.book_name AS "Book Name",
    COUNT(i.issuance_id) AS "# of times borrowed",
    COUNT(DISTINCT i.mem_id) AS "# of members that borrowed"
FROM 
    Issuance i
JOIN 
    Book b ON i.book_id = b.book_id
GROUP BY 
    b.book_id, b.book_name
ORDER BY 
    COUNT(i.issuance_id) DESC
LIMIT 10;





4. Write a query to get member name who has borrowed the most books and number of 
books borrowed
SELECT 
    m.mem_name AS "Member Name",
    COUNT(i.book_id) AS "# of books borrowed"
FROM 
    Issuance i
JOIN 
    Member m ON i.mem_id = m.mem_id
GROUP BY 
    m.mem_id, m.mem_name
ORDER BY 
    COUNT(i.book_id) DESC
LIMIT 1;

## 1. Explain the difference between a stack and a queue. Provide real life examples of real-life scenarios where each of them are used appropriately.
- A stack is a Last-In-First-Out (LIFO) data structure, meaning that the last element added to the stack is the first one to be removed. A queue is a First-In-First-Out (FIFO) data structure, meaning that the first element added to the queue is the first one to be removed.
- [Stack] When you perform actions like typing, deleting, or formatting in a document editor or text editor, each action is added to a stack. Pressing "Undo" removes the last action performed, effectively popping it off the stack.
- [Queue] A queue is a natural model for representing waiting lines, such as lines at a supermarket checkout. Customers or individuals join the back of the line (enqueue), and the person at the front of the line is served or processed (dequeue) first.

## 2. What is the difference between an array and a linked list? Provide advantages and disadvantages of each data structure.
- Array:
    ---
    - In an array you can access the element by using an index.
    - [Advantage] Accessing elements by index is very fast and efficient. That means is has a constant-time access.
    - [Advantage] Elements in an array are stored in contiguous memory locations, which can lead to better cache performance.
    - [Disadvantage] Arrays have a fixed size, so resizing can be inefficient.
    - [Disadvantage] Insertion and deletion operations may require shifting elements, resulting in slower performance.
- Linked list:
    ---
    - Linked lists can be singly linked (each node points to the next node) or doubly linked (each node points to both the next and previous nodes).
    - [Advantage] Linked lists can grow or shrink dynamically without requiring resizing operations.
    - [Advantage] Insertion and deletion operations can be performed efficiently, especially at the beginning or end of the list.
    - [Disadvantage] Accessing elements by index in a linked list requires traversing the list from the beginning, which can be slow for large lists.
    - [Disadvantage] Linked lists require additional memory overhead for storing references to the next (and possibly previous) nodes.

## 3. What is HTTP? How is it different from HTTPS?
- HTTP (Hypertext Transfer Protocol) it is a stateless protocol, meaning that each request from a client to the server is independent and unrelated to any previous requests
- HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP that adds a layer of security by using SSL/TLS protocols to encypt data transmitted between the client and the server.

## 4. Can you give some examples of common HTTP response codes?
- 200 OK
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

## 5. What is the difference between authorization and authentication?
- Authentication is the process of verifying the identity of a user.
- Authorization, on the other hand, is the process of determining what actions or resources a user is allowed to access after they have been authenticated.

## 6. How would you explain to a 5-year-old how the WWW works?
Imagine the World Wide Web is like a big playground with lots of different toys and games. Each toy or game is like a website on the internet.

Now, to visit a website, you need a special tool called a web browser. It's like a magic portal that takes you to any toy or game you want to play with on the playground.

When you type a website's name into the web browser, it sends a message to a special place called a server. The server is like a big toy chest where all the toys and games are kept.

The server gets the message and sends back the website to your web browser, just like a friend handing you the toy you asked for on the playground.

Then, you can see the website on your computer or phone screen, and you can click on different things to explore and play!
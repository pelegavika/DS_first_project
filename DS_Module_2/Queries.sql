/*
delete from tasks
delete from users
delete from status 
*/

/*Отримати всі завдання певного користувача*/
SELECT * FROM tasks WHERE user_id = 65;

/*Вибрати завдання за певним статусом.*/
SELECT * FROM tasks WHERE status_id = 10;

/*Оновити статус конкретного завдання*/
UPDATE tasks 
SET status_id = 11
WHERE id = 180;

/*Отримати список користувачів, які не мають жодного завдання.*/
SELECT * FROM users 
WHERE id NOT IN (SELECT user_id
    FROM tasks);


/*Додати нове завдання для конкретного користувача.*/  
 INSERT INTO tasks (user_id, title , description, status_id) VALUES (60,'sql','зробити домашню роботу', 10);
 
/*Отримати всі завдання, які ще не завершено.*/
SELECT * FROM tasks 
WHERE status_id NOT IN (SELECT id 
    FROM status
    WHERE name = 'completed' );
    
  /*Видалити конкретне завдання.*/ 
 DELETE FROM tasks WHERE id = 193;
 
 /*Знайти користувачів з певною електронною поштою.*/ 
SELECT * FROM users WHERE email LIKE 'salazarcourtney%';

 /*Оновити ім'я користувача*/ 
UPDATE users SET fullname = 'John Smith'
WHERE id = 67;

 /*Отримати кількість завдань для кожного статусу.*/
SELECT COUNT(status_id) AS total_count, status_id 
FROM tasks
GROUP BY status_id 

 /*Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.*/
SELECT t.id, t.title , t.description , u.email AS email
FROM tasks AS t
INNER JOIN users AS u ON u.id = t.user_id 
WHERE u.email LIKE '%@gmail.com';


INSERT INTO tasks (user_id, title , status_id) VALUES (60,'test', 11);
 /*Отримати список завдань, що не мають опису.*/
SELECT * FROM tasks 
WHERE description is NULL ;

 /*Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. */
SELECT t.id, t.title , t.description , u.fullname, s.name AS name
FROM tasks AS t
INNER JOIN users AS u ON u.id = t.user_id 
INNER JOIN status AS s ON s.id = t.status_id 
WHERE s.name ='in progress';


INSERT INTO users (fullname, email) VALUES ('Tom Soyer', 'rrr@com');
 /*Отримати користувачів та кількість їхніх завдань.*/
SELECT COUNT(tasks.id) AS task_count, u.id, u.fullname
FROM users AS u
LEFT JOIN tasks ON u.id = tasks.user_id 
GROUP BY u.id, u.fullname 


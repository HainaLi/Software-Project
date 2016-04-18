
 
SELECT 
	question.Title AS question_title, 
    question.Body AS question_body, 
    question.Score AS question_score, 
    question.AnswerCount AS question_answercount, 
    question.CommentCount AS question_commentcount,
      CASE
			WHEN (patindex('%</code></pre>%', answer.body) = 0)
				THEN 0
			ELSE 1
		END as question_hascode,
        datediff(day, question.CreationDate, GETDATE()) as question_age,
	answer.Body AS answer_body,
	answer.Score AS answer_score,
	answer.CommentCount AS answer_commentcount,
    question_author.Id AS question_author_id,
	question_author.Reputation as question_author_reputation,
	(question_author.UpVotes - question_author.DownVotes) as question_author_score,
	question_author.CreationDate as question_author_creationdate,
    answer_author.Id AS answer_author_id,
	answer_author.Reputation as answer_author_reputation,
	(answer_author.UpVotes - answer_author.DownVotes) as answer_author_score,
	answer_author.CreationDate as answer_author_creationdate,
	question.ViewCount AS viewcount
	
FROM 
	Posts AS question 
INNER JOIN
	Posts AS answer
	ON answer.Id = question.AcceptedAnswerId
    
INNER JOIN
	Users AS question_author
	ON question_author.id = question.OwnerUserId
INNER JOIN
	Users AS answer_author
	ON answer_author.id = answer.OwnerUserId
WHERE datediff(day, question.CreationDate, GETDATE()) BETWEEN 365 and 700
ORDER BY datediff(day, question.CreationDate, GETDATE()) ASC
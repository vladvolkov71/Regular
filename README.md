# Домашнее задание к лекции 2.2 «Regular expressions»

Ваша задача: привести в порядок адресную книгу, используя регулярные выражения.  
Структура данных будет всегда такая:   
`lastname,firstname,surname,organization,position,phone,email`  

Предполагается, что:
* телефон и e-mail у одного человека может быть только один;
* если совпали одновременно Фамилия и Имя, это точно один и тот же человек (даже если не указано его отчество).

Ваша задача:
1. Поместить Фамилию, Имя и Отчество человека в поля `lastname`, `firstname` и `surname` соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О. 
2. Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999. 
3. Объединить все дублирующиеся записи о человеке в одну.

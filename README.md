#Django Project for Iot With ESP8266

This is a very simple to use project.<br/>
Download the files and install the requirements.<br/>
To run: python manage.py runserver <br/>

I invite you to see a deployed example, use it like a sand box:<br/>
URL: https://nahueltest.azurewebsites.net/api/luces<br/>
username for access and API: uno<br/>
Pass:03011988 <br/>
If you ant the ESP266 code I can give you.


Routes:<br/>
1) Light list: /api/luces/<br/>
2) Light by indicator: /api/estado/light_id <br/>
3) There are paths to create, update, delete lights. API REST <br/>
4) There is a server server monitor in api/panel<br/>

API REST Format:<br/>
application/json<br/>
<br/>
          {<br/>
              "Luz": 1,<br/>
              "encendido": false,<br/>
              "Ip": "192.168.1.11",<br/>
              "descripcion": "la luz primigenia"<br/>
          }<br/>

![image](https://user-images.githubusercontent.com/37676359/195884113-39a825b7-a2f8-415e-b989-79b538f5e89b.png)

# Lab 8

## Example 00:

![example00](example00.PNG)

<hr />

## Example 01:

### Running ubuntu in docker

![example01a](example01a.PNG)

### Creating a file with VIM

![example01b](example01b.PNG)

### Installing Cowsay

![example01c](example01c.PNG)

<hr />

## Example 02:

### Starting Mongo

![example02a](example02a.PNG)

![example02b](example02b.PNG)

### Setting up Rocket Chat

![example02c](example02c.PNG)

![example02d](example02d.PNG)

## Example 03:

### Building and running a DockerFile

![example03a](example03a.PNG)

![example03b](example03b.PNG)

## Example 04:

### Creating a Dockerfile for the app

 ![example04a](example04a.PNG)

 Note that when you run the DockerFile it crashes because there is not MongoDB server setup, I think this is the expected result.

### Creating docker-compose file

![example04b](example04b.PNG)

![example04c](example04c.PNG)

To get the server to work I had to change the port, I guess something is running on 1337

Responses from server:

        [
        {
            "text": "hello",
            "createdAt": "2015-11-08T13:15:15.363Z",
            "updatedAt": "2015-11-08T13:15:15.363Z",
            "id": "5638b363c5cd0825511690bd" 
        },
        {
            "text": "hola",
            "createdAt": "2015-11-08T13:15:45.774Z",
            "updatedAt": "2015-11-08T13:15:45.774Z",
            "id": "5638b381c5cd0825511690be"
        }
        ]


And 

        [
        {
            "text": "hey",
            "createdAt": "2015-11-08T13:15:15.363Z",
            "updatedAt": "2015-11-08T13:19:40.179Z",
            "id": "5638b363c5cd0825511690bd"
        }
        ]
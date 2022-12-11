# awsome_resume_with_flask
To use Docker follow this commands

## Build docker image

{% highlight python %}

  $ docker build --tag app .

{% endhighlight %}


## To check the docker images list

{% highlight python %}

  $ docker images

{% endhighlight %}

## Run Docker images as standalone program

{% highlight python %}

  $ docker run -d -p 5000:5000 app

{% endhighlight %}

Note: Here app is the container we have created in Dockerfile


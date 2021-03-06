![Geospartial MapReduce](docs/geospatial_mapreduce.png)

### Install Gdal
Get gdal development libraries:
```shell script
$ sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
$ sudo apt-get update
$ sudo apt-get install libgdal-dev
$ sudo apt-get install python3-dev
$ sudo apt-get install gdal-bin python3-gdal
```

## Install virtual enviroment
```shell script
$ sudo apt-get install virtualenv
```

### Create and activate a virtual environment
```shell script
$ virtualenv env -p python3
$ source env/bin/activate
```

### Install Requirements
```shell script
(env)$ pip3 install -r requirements.txt
```

### Install GDAL Python lib
```shell script
(env)$ pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
```

### Dataset
[Download link](https://drive.google.com/drive/folders/1TZWfhc6KJYfkB58FXdp-DzxPJA6ZaSgT?usp=sharing)

```shell script
mkdir data/
ls data/
    LC08_220069_20190213.tif
    LC08_220069_20190520.tif
    ...
```

### Execute
```shell script
(env)$ python3 main.py
```

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">
    <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" />
</a>
<br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

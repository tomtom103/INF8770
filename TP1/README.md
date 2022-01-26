# First Lab of the INF8770 class

The files in the `assets/` folder are used to test our implementations of the LZ77 and RLE algorithms in python. 

# Hypothesis:

Our hypotheses are as follow:


# How our data was generated:

## Binary

For the binary files, we use the default random generator of the operating system

```bash
$ cat /dev/urandom | head -c {size} > assets/binary/{size}
```

TODO: Talk about entropy

## PNG / JPEG

Both PNG and JPEG files were taken from the online service [File Examples](https://file-examples.com/)

This allows us to have an unbiased choice towards the images. They can also be downloaded in multiple sizes.

For this test, both images are `500kB` in size.

## Text

In order to test the text using both LZ77 and LRE, we have decided to first take data samples from English literature, our first file `long_en.txt` is from `Dr Jekyll and Mr Hyde` and the second file `short_en.txt` is from `Evelina`. 

We have also generated two sizes of sequences or long characters, this was done the `/dev/urandom` generator. The command goes aas follows:

```bash
$ cat /dev/urandom | tr -dc A-Za-z0-9 | head -c {size} assets/text/filename.txt
```

This command was inspired from an answer found on the [Unix StackExchange](https://unix.stackexchange.com/questions/230673/how-to-generate-a-random-string)

# WAV .wav

Same as the PNG / JPEG files, the `WAV` file was taken from [File Examples](https://file-examples.com/)
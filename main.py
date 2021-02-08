from random import randint

from PIL import Image

img_source = Image.open('original.bmp')
height, width = img_source.size
c_zero_array = [[0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
c_one_array = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0],
               [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
source_array = []
first_array = []
second_array = []
if (height)!=(width):
  print("Archive must have same height and width.")
  else:
  for row in range(height):
      for col in range(width):
          number = randint(0, 5)
          a = img_source.getpixel((col, row))
          if a == 255:
              # white
              for i in c_zero_array[number]:
                  first_array.append(i)
                  second_array.append(i)
          if a == 0:
              # black
              for i in c_one_array[number]:
                  first_array.append(i)
              for i in c_one_array[number + 6]:
                  second_array.append(i)
          source_array.append(a)

  img_first = Image.new("1", (height * 2, width * 2), "white")
  img_second = Image.new("1", (height * 2, width * 2), "white")

  height2, width2 = img_first.size

  column2 = 0
  row = 0
  for index in range(0, height2//2):

      col = 0
      for column in range(column2, column2 + width2 * 2, 4):
          if first_array[column] == 0:
              img_first.putpixel((col, row), 255)
          else:
              img_first.putpixel((col, row), 0)
          if first_array[column + 1] == 0:
              img_first.putpixel((col + 1, row), 255)
          else:
              img_first.putpixel((col + 1, row), 0)
          col += 2

      col = 0
      for column in range(column2, column2 + width2 * 2, 4):
          if second_array[column] == 0:
              img_second.putpixel((col, row), 255)
          else:
              img_second.putpixel((col, row), 0)
          if second_array[column + 1] == 0:
              img_second.putpixel((col + 1, row), 255)
          else:
              img_second.putpixel((col + 1, row), 0)
          col += 2
      row += 1

      col = 0
      for column in range(column2 + 2, column2 + width2 * 2, 4):
          if first_array[column] == 0:
              img_first.putpixel((col, row), 255)
          else:
              img_first.putpixel((col, row), 0)
          if first_array[column + 1] == 0:
              img_first.putpixel((col + 1, row), 255)
          else:
              img_first.putpixel((col + 1, row), 0)
          col += 2

      col = 0
      for column in range(column2 + 2, column2 + width2 * 2, 4):
          if second_array[column] == 0:
              img_second.putpixel((col, row), 255)
          else:
              img_second.putpixel((col, row), 0)
          if second_array[column + 1] == 0:
              img_second.putpixel((col + 1, row), 255)
          else:
              img_second.putpixel((col + 1, row), 0)
          col += 2
          column2 = column + 2
      row += 1

  img_first.save('1.bmp')
  img_second.save('2.bmp')

  #combined 1&2 construction:
  
  img_out = Image.new("1", (height * 2, width * 2), "white")

  for row in range(height * 2):
      for col in range(width * 2):
          a = img_first.getpixel((col, row))
          b = img_second.getpixel((col, row))
          if a == 255 and b == 255:
              img_out.putpixel((col, row), 255)
          else:
              img_out.putpixel((col, row), 0)

  img_out.save('final.bmp')

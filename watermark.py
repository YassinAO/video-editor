import moviepy.editor as mp

# ToDo: Do some research on how the quality of the exported video can be improved

file_path = input('Enter path to file: ')

# Used to rename the new file
index = file_path.find('.mp4')
new_filename = file_path[:index] + '-watermark.mp4'

video = mp.VideoFileClip(file_path)

# Add a watermark with specific styling
watermark = (mp.ImageClip("assets/watermark/watermark.png")
          .set_duration(video.duration)
          .resize(height=75)
          .margin(right=8, bottom=8, opacity=0)
          .set_pos(("right","bottom")))

# Overlay the watermark clip on the first video clip
final_video = mp.CompositeVideoClip([video, watermark])

# Write the result to a file (many options available!)
final_video.write_videofile(new_filename) 

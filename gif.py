import moviepy.editor as mp

def time_symetrize(video):
    return mp.concatenate([video, video.fx(mp.vfx.time_mirror)])

file_path = input('Enter path to file: ')

# Used to rename the new file to .gif
index = file_path.find('.mp4')

start_time = int(input('Enter start time: '))
end_time = int(input('Enter end time: '))

video = (mp.VideoFileClip(file_path)
        .subclip((start_time),(end_time))
        .resize(0.2)
        .fx(time_symetrize)) # Returns the clip played forward then backwards

new_filename = file_path[:index] + '.gif'
final_gif = mp.CompositeVideoClip([video])      

final_gif.write_gif(new_filename)

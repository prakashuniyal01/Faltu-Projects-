import json


file_name = 'youtube_videos.txt'

# load data from file
def load_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found. Creating new file.")
        return []
    
    
def save_data(videos):
    with open(file_name, 'w') as f:
        json.dump(videos, f)

# list videos should
def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}, {video['name']}, Duration:  {video['time']} ")
    print("\n")
    print("*" * 50)

# all videos add
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time : ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("Video added successfully.")
    

# update all videos
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video to update: ")) 
    if 1 <= index <= len(videos):
        name = input("Enter the video to update'")
        time = input("Enter video time : ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data(videos)
    else:
        print("Invalid index.")
        


#  delete video
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video to delete: ")) 
    if 1 <= index <= len(videos):
        del videos[index-1]
        # videos.pop(index - 1)
        save_data(videos)
        print("Video deleted successfully.")
    else:
        print("Invalid index.")


def main():

    videos = load_data()
    while True:
        print("\n youtube managers")
        print("1. List a all youtube video")
        print('2 add a youtube video')
        print('3 update a youtube video')
        print('4 remove a youtube video')
        print('5. Exit')
        choice = input('Enter your choise: ')
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print('Exiting...')
                break
            case _:
                print('Invalid choice. Please try again.')


if __name__ ==  "__main__":
    main()
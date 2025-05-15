import os
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from PIL import Image

def editar_varios_videos(nomes_videos_str):
    image_path = "Images/subscribe.png"
    resized_image_path = "Images/subscribe_resized.png"
    output_dir = "VidiosEdited"
    nomes_videos = nomes_videos_str.split()

    os.makedirs(output_dir, exist_ok=True)

    try:
        pil_img = Image.open(image_path)
        width, height = pil_img.size
        new_height = 120 
        new_width = int(width * new_height / height)
        pil_img = pil_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        pil_img.save(resized_image_path)
    except Exception as e:
        print(f"❌ Erro ao redimensionar a imagem: {e}")
        return

    for nome_video in nomes_videos:
        video_path = f"Vidios/{nome_video}"
        output_path = os.path.join(output_dir, f"editado_{nome_video}")

        try:
            print(f"Processando: {video_path}")

            video = VideoFileClip(video_path)

            imagem = (ImageClip(resized_image_path)
                      .set_duration(2)   
                      .set_start(1)      
                      .set_position("center"))

            video_final = CompositeVideoClip([video, imagem])

            video_final.write_videofile(output_path, codec="libx264", audio_codec="aac")

            print(f"✅ Vídeo salvo como: {output_path}\n")

        except Exception as e:
            print(f"❌ Erro ao processar {nome_video}: {e}")

if __name__ == "__main__":
    videos = input("Digite os nomes dos vídeos separados por espaço: ")
    editar_varios_videos(videos)

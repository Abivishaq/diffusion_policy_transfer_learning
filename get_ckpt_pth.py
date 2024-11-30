import os
def get_ckpt_pth(num_demos):
    run_dir = "/home/abivishaq/projects/GT_coursework/fall_2024/DL/diffusion_policy/runs"
    
    folders = os.listdir(run_dir)
    for folder in folders:
        if folder.startswith("PickCube-v1__train__"):
            detial_file_pth = os.path.join(run_dir, folder, "exp_details.txt")
            with open(detial_file_pth, "r") as f:
                lines = f.readlines()
                demo_line = lines[0]
                num_demos_in_folder = int(demo_line.split(":")[-1])
                print(num_demos_in_folder)
                print(demo_line)
                if num_demos_in_folder == num_demos:
                    ckpt_pth = os.path.join(run_dir, folder, "checkpoints", "best_eval_success_at_end.pt")
                    print(ckpt_pth)
                    print(os.path.exists(ckpt_pth)) 
                    return ckpt_pth
            
    return None

if __name__ == "__main__":
    get_ckpt_pth(50)
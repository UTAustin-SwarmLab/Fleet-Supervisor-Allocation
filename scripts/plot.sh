plot() {

    local env_name=$1

    directory_to_plot=/home/oguzhan-admin/Fleet-Supervisor-Allocation/logs/
    subdirectory_to_plot="${env_name}_final_experiments/scarce"
    full_directory_path="${directory_to_plot}${subdirectory_to_plot}"
    directory_to_send_the_plot=/home/oguzhan-admin/Fleet-Supervisor-Allocation/finalized_plots/humanoid/scarce
    plotting_code_directory=plotting/plot_ege_color.py

    cd /home/oa5983/ege/Fleet-Supervisor-Allocation

    python $plotting_code_directory $full_directory_path cumulative_successes
    python $plotting_code_directory $full_directory_path cumulative_human_actions
    python $plotting_code_directory $full_directory_path cumulative_hard_resets
    python $plotting_code_directory $full_directory_path cumulative_idle_time
    python $plotting_code_directory $full_directory_path ROHE

    cd /home/oa5983/ege/Fleet-Supervisor-Allocation
    mv cumulative_successes.jpg "${plot_name}_cumulative_successes.jpg"
    mv cumulative_human_actions.jpg "${plot_name}_cumulative_human_actions.jpg"
    mv cumulative_hard_resets.jpg "${plot_name}_cumulative_hard_resets.jpg"
    mv cumulative_idle_time.jpg "${plot_name}_cumulative_idle_time.jpg"
    mv ROHE.jpg "${plot_name}_ROHE.jpg"

    mv *cumulative* $directory_to_send_the_plot
    mv *ROHE* $directory_to_send_the_plot
}


plot Humanoid

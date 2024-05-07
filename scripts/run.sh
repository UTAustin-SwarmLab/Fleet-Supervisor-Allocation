plot() {

    local plot_name=$1

    directory_to_plot=/nas/oguzhan/fleet_supervision/logs/cur_20_hum/
    subdirectory_to_plot=CUR
    #full_directory_path="${directory_to_plot}${subdirectory_to_plot}"
    full_directory_path="${directory_to_plot}"
    directory_to_send_the_plot=/home/oa5983/ege/Fleet-Supervisor-Allocation/all_plots/experiment_plots
    plotting_code_directory=plotting/plot_ablition_studies.py

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

    cd scripts
}


plot CUR_25 # Name of the folder that has the results

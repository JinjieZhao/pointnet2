cd utils
bash compile_render_balls_so.sh

cd ..
cd tf_ops

cd 3d_interpolation
bash tf_interpolate_compile.sh
cd ..

cd grouping
bash tf_grouping_compile.sh
cd ..

cd sampling
bash tf_sampling_compile.sh

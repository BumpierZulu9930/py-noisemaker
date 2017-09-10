import click
import tensorflow as tf

from noisemaker.util import save

import noisemaker.cli as cli
import noisemaker.generators as generators
import noisemaker.recipes as recipes


@click.command(help="""
        Noisemaker - Visual noise generator

        https://github.com/aayars/py-noisemaker
        """, context_settings=cli.CLICK_CONTEXT_SETTINGS)
@cli.freq_option()
@cli.width_option()
@cli.height_option()
@cli.channels_option()
@cli.octaves_option()
@cli.ridges_option()
@cli.deriv_option()
@cli.deriv_alpha_option()
@cli.post_deriv_option()
@cli.interp_option()
@cli.sin_option()
@cli.distrib_option()
@cli.corners_option()
@cli.mask_option()
@cli.lattice_drift_option()
@cli.vortex_option()
@cli.warp_option()
@cli.warp_octaves_option()
@cli.warp_interp_option()
@cli.warp_freq_option()
@cli.post_reflect_option()
@cli.reflect_option()
@cli.post_refract_option()
@cli.refract_option()
@cli.reindex_option()
@cli.clut_option()
@cli.clut_range_option()
@cli.clut_horizontal_option()
@cli.voronoi_option()
@cli.voronoi_func_option()
@cli.voronoi_nth_option()
@cli.voronoi_alpha_option()
@cli.voronoi_refract_option()
@cli.voronoi_inverse_option()
@cli.dla_option()
@cli.dla_padding_option()
@cli.point_freq_option()
@cli.point_distrib_option()
@cli.point_corners_option()
@cli.point_generations_option()
@cli.point_drift_option()
@cli.wormhole_option()
@cli.wormhole_stride_option()
@cli.wormhole_kink_option()
@cli.worms_option()
@cli.worms_density_option()
@cli.worms_duration_option()
@cli.worms_stride_option()
@cli.worms_stride_deviation_option()
@cli.worms_kink_option()
@cli.worms_bg_option()
@cli.erosion_worms_option()
@cli.sobel_option()
@cli.outline_option()
@cli.normals_option()
@cli.posterize_option()
@cli.bloom_option()
@cli.glitch_option()
@cli.vhs_option()
@cli.crt_option()
@cli.scan_error_option()
@cli.snow_option()
@cli.dither_option()
@cli.aberration_option()
@cli.emboss_option()
@cli.shadow_option()
@cli.edges_option()
@cli.sharpen_option()
@cli.unsharp_mask_option()
@cli.invert_option()
@cli.rgb_option()
@cli.hsv_range_option()
@cli.hsv_rotation_option()
@cli.hsv_saturation_option()
@cli.input_dir_option()
@cli.wavelet_option()
@cli.name_option()
@click.pass_context
def main(ctx, freq, width, height, channels, octaves, ridges, sin, wavelet, lattice_drift, vortex, warp, warp_octaves, warp_interp, warp_freq, reflect, refract, reindex,
         post_reflect, post_refract, clut, clut_horizontal, clut_range, worms, worms_density, worms_duration, worms_stride, worms_stride_deviation,
         worms_bg, worms_kink, wormhole, wormhole_kink, wormhole_stride, sobel, outline, normals, post_deriv, deriv, deriv_alpha, interp, distrib, corners, mask, posterize,
         erosion_worms, voronoi, voronoi_func, voronoi_nth, voronoi_alpha, voronoi_refract, voronoi_inverse,
         glitch, vhs, crt, scan_error, snow, dither, aberration, bloom, rgb, hsv_range, hsv_rotation, hsv_saturation, input_dir,
         dla, dla_padding, point_freq, point_distrib, point_corners, point_generations, point_drift,
         name, **convolve_kwargs):

    shape = [height, width, channels]

    tensor = generators.multires(freq=freq, shape=shape, octaves=octaves, ridges=ridges, sin=sin, wavelet=wavelet, lattice_drift=lattice_drift,
                                 reflect_range=reflect, refract_range=refract, reindex_range=reindex,
                                 post_reflect_range=post_reflect, post_refract_range=post_refract,
                                 clut=clut, clut_horizontal=clut_horizontal, clut_range=clut_range,
                                 with_worms=worms, worms_density=worms_density, worms_duration=worms_duration,
                                 worms_stride=worms_stride, worms_stride_deviation=worms_stride_deviation, worms_bg=worms_bg, worms_kink=worms_kink,
                                 with_wormhole=wormhole, wormhole_kink=wormhole_kink, wormhole_stride=wormhole_stride, with_erosion_worms=erosion_worms,
                                 with_voronoi=voronoi, voronoi_func=voronoi_func, voronoi_nth=voronoi_nth,
                                 voronoi_alpha=voronoi_alpha, voronoi_refract=voronoi_refract, voronoi_inverse=voronoi_inverse,
                                 with_dla=dla, dla_padding=dla_padding, point_freq=point_freq, point_distrib=point_distrib, point_corners=point_corners,
                                 point_generations=point_generations, point_drift=point_drift,
                                 with_outline=outline, with_sobel=sobel, with_normal_map=normals, post_deriv=post_deriv, deriv=deriv, deriv_alpha=deriv_alpha,
                                 spline_order=interp, distrib=distrib, corners=corners, mask=mask,
                                 warp_range=warp, warp_octaves=warp_octaves, warp_interp=warp_interp, warp_freq=warp_freq,
                                 posterize_levels=posterize, vortex_range=vortex,
                                 hsv=not rgb, hsv_range=hsv_range, hsv_rotation=hsv_rotation, hsv_saturation=hsv_saturation, input_dir=input_dir,
                                 with_aberration=aberration, with_bloom=bloom, **convolve_kwargs)

    tensor = recipes.post_process(tensor, shape=shape, freq=freq, with_glitch=glitch, with_vhs=vhs, with_crt=crt, with_scan_error=scan_error, with_snow=snow, with_dither=dither)

    with tf.Session().as_default():
        save(tensor, name)

    print(name)
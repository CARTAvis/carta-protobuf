.. _data-streaming:

Data streaming
--------------

While some data flows can be described by a simple request/response approach, such as retrieving file lists or file information, other data flows require an asynchronous data stream approach. This need arises from situations where a single state change command corresponds to more than one response from the backend. For example, changing image channel would require each spatial profile associated with the active image channel to be updated, possibly resulting in more than one :carta:ref:`SPATIAL_PROFILE_DATA` messages. Moving a region would require updating any analytics associated with the region. It is the backend’s responsibility to correctly determine which analytic data needs to be updated whenever a control message is sent. It is essential that the backend only recalculates and sends data when needed. In order to do this, the backend must keep track of any updates to region requirements, and use these requirements to determine whether updates are needed. Region requirements will reflect the current frontend UI configuration. Changes to the frontend UI configuration (such as changing between “average” and “max” on a spectral profile widget) will result in new region requirements being sent to the backend, which will then be processed, resulting in new data being sent to the frontend when required.

Some examples of possible resultant data streams for control messages are given below:

-  :carta:ref:`SET_IMAGE_CHANNELS`: Changing either the channel or the Stokes parameter would require new image data to be sent, for both raster and contour images. Changing from one channel to another in the same Stokes cube could result in histograms, spatial profiles or region stats to require updating. Changing to a new stokes cube could also require spectral profiles to be updated. These updates will depend on the defined regions and defined region requirements.
-  :carta:ref:`START_ANIMATION`: Starting an animation will require new image data for each frame. In addition, since the animation playback may be across file, Stokes or channel parameters, the same data streams as those arising from :carta:ref:`SET_IMAGE_CHANNELS` can occur.
-  :carta:ref:`SET_CURSOR`: Updating the cursor position is a special case of updating a region. As the cursor position is a point region, only spectral data and spatial data can require an update.
-  :carta:ref:`SET_REGION`: Creating a region will not result in any data streams, as the region’s requirements will be empty by default. However, updating a regions parameters (other than region name) could result in spatial profiles (for open regions), spectral profiles, region stats and histograms (for closed and point regions) to be updated.
-  :carta:ref:`SET_STATS_REQUIREMENTS`: Updating stats requirements for a region can result in region stats data being updated.
-  :carta:ref:`SET_HISTOGRAM_REQUIREMENTS`: Updating histogram requirements for a region (either by updating the channel required for the histogram or by changing the histogram bin number) can result in histogram data being updated.
-  :carta:ref:`SET_SPATIAL_REQUIREMENTS`: Updating spatial profile requirements for a region can result in spatial profile data being updated.
-  :carta:ref:`SET_SPECTRAL_REQUIREMENTS`: Updating spectral profile requirements for a region (either by changing the coordinate required, such as “Qz” or “Uz”, or by changing the statistic type used to generate the profile) can result in spectral profile data being updated.
-  :carta:ref:`SET_CONTOUR_PARAMETERS`: Updating contour parameters for a file will result in new contour image data being required.


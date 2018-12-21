$.ajax({
    type: "POST",
    url: "https://www2.onlinevideoconverter.com/webservice",
    async: true,
    cache: false,
    data: {
        function: 'validate', // 'validate' -> processVideo
        args: getParameters()
    },
    dataType: "json",
    success: function(a) {
        console.log(a);
    },
    error: function(a, b, c) {}
})

function getParameters() {
    return {
        advSettings: false,
        aspectRatio: "-1",
        audioBitrate: 0,
        audioFormat: undefined,
        audioFrequency: 0,
        channel: "stereo",
        custom_resx: -1,
        custom_resy: -1,
        dummy: "1",
        endTo: "-1",
        fromConvert: "urlconverter",
        id_process: undefined,
        keyHash: undefined,
        nbRetry: 0,
        oldServerIds: [],
        requestExt: "mp4",
        serverId: undefined,
        serverUrl: undefined,
        startFrom: "-1",
        title: undefined,
        uploadPath: undefined,
        urlEntryUser: "https://youtu.be/x2pXP0U__6Y",
        videoBitrate: undefined,
        videoResolution: "-1",
        volume: 0
    }
}
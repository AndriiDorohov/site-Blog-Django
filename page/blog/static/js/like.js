// $(".unlike-button").click(function () {
//   var articleId = $(this).data("article-id");
//   var unlikeButton = $(this);

//   $.ajax({
//     url: `/unlike/${articleId}/`,
//     method: "POST",
//     data: { article_id: articleId },
//     success: function (data) {
//       if (data.status === "success") {
//         var likeCount = unlikeButton.siblings(".like-count");
//         likeCount.text(parseInt(likeCount.text()) - 1);
//       }
//     },
//   });
// });
//

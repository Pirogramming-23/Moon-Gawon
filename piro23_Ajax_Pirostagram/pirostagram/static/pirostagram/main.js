console.log("✅ main.js 불러와짐");

// CSRF 토큰 가져오기 함수
window.getCookie = function (name) {
    const cookies = document.cookie.split(';');
    for (let c of cookies) {
        const [key, value] = c.trim().split('=');
        if (key === name) return decodeURIComponent(value);
    }
    return null;
};

// 좋아요 기능
const likePost = async (postId) => {
    console.log("👍 좋아요 요청");
    const res = await fetch("/like_ajax/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: `post_id=${postId}`
    });

    const data = await res.json();
    document.getElementById(`like-count-${postId}`).innerText = data.like_count;
    const btn = document.getElementById(`like-btn-${postId}`);
    if (btn) {
        btn.innerText = data.liked ? "❤️" : "🤍";
    }
};


document.addEventListener("DOMContentLoaded", () => {
    // 댓글 버튼 전체에 이벤트 걸기
    document.querySelectorAll(".comment-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const postId = btn.getAttribute("data-post-id");
            createComment(postId);
        });
    });
});
// 댓글 작성
window.createComment = function(postId) {
    console.log("🧪 댓글 생성 시작");
    const input = document.getElementById(`comment-input-${postId}`);

    if (!input) {
        console.error(`❌ input(comment-input-${postId}) not found`);
        return;
    }

    const content = input.value.trim();

    if (!content) return;

    fetch("/comment/create/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: `post_id=${postId}&content=${encodeURIComponent(content)}`
    })
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById(`comment-list-${postId}`);
        if (!list) {
            console.error("❌ comment list not found");
            return;
        }

        const newComment = document.createElement("li");
        newComment.id = `comment-${data.id}`;
        newComment.innerHTML = `<b>${data.user}</b>: ${data.content} 
            <button onclick="deleteComment(${data.id})">삭제</button>`;
        list.prepend(newComment);

        input.value = "";
    })
    .catch(err => {
        console.error("❌ 댓글 추가 실패", err);
    });
}

// 댓글 삭제
window.deleteComment = function(commentId) {
    fetch("/comment/delete/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: `comment_id=${commentId}`
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const el = document.getElementById(`comment-${commentId}`);
            if (el) el.remove();
        }
    });
}

// main.js 끝부분
window.createComment = createComment;
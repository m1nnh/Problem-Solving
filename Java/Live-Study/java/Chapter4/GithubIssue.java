package Chapter4;

import org.kohsuke.github.*;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.*;

public class GithubIssue {
    //personal token need to secret
    private static final String MY_PERSONAL_TOKEN = "SERCRET_KEY";

    public static void main(String[] args) throws IOException {
        
        GitHub github = new GitHubBuilder().withOAuthToken(MY_PERSONAL_TOKEN).build();

        //Repository 연결
        GHRepository repo = github.getRepository("whiteship/live-study");

        //IssueState ALL, OPEN, CLOSED
        List<GHIssue> issues = repo.getIssues(GHIssueState.ALL);
        Map<String, Integer> participant = new HashMap<>();

        // 1-18개 이슈
        for (GHIssue issue : issues) {
            Set<String> onlyOneParticipant = new HashSet<>();

            //댓글 한개 이상 단 경우 유저이름 중복 제거
            for (GHIssueComment comment : issue.getComments()) {
                onlyOneParticipant.add(comment.getUser().getName());
            }

            //카운트 증가해주기
            for (String name : onlyOneParticipant) {
                if(participant.containsKey(name)){
                    participant.replace(name,participant.get(name)+1);
                    continue;
                }
                participant.put(name,1);
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //참여율 출력
        for(String name : participant.keySet()){
            double rate = (double)(participant.get(name) * 100) / issues.size();
            bw.write("name : " + name);
            bw.write(", Participation Rate : "+String.format("%.2f",rate)+"%");
            bw.newLine();
        }
        bw.close();
    }

}

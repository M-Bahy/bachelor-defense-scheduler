import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

public class algo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<triple> studentsToBeAssigned = new ArrayList<>();
        HashSet<String> internalNames = new HashSet<>();
        HashSet<String> externalNames = new HashSet<>();
        HashMap<String, Integer> externalSlots = new HashMap<>();
        String line = "";
        String splitBy = ",";
        try {
            BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\Youssef Shawky\\IdeaProjects\\ACM\\src\\MET " +
                    "Bachelor Thesis Presentations schedule.csv"));
            while ((line = br.readLine()) != null)   //returns a Boolean value
            {
                String[] employee = line.split(splitBy);    // use comma as separator
                studentsToBeAssigned.add(new triple(Integer.parseInt(employee[0]), employee[1], employee[2], employee[4], employee[3]));
                internalNames.add(employee[3]);
                externalNames.add(employee[4]);


            }
            // studentsToBeAssigned is done

            for (String externalName : externalNames) {
                externalSlots.put(externalName, 0);
            }
            for (triple triple : studentsToBeAssigned) {
                externalSlots.put(triple.external, externalSlots.get(triple.external) + 1);
            }
            int idx = 0;
            Pair[] numberOfSlots = new Pair[externalSlots.size()];
            for (String s : externalSlots.keySet()) {
                numberOfSlots[idx++] = new Pair(s, externalSlots.get(s));
            }
            // number of slots is done
            int numberOfDays = sc.nextInt();

            int[] arr = new int[numberOfDays * 15];
            Arrays.fill(arr, 1);
            HashMap<String, int[][]> internalAvailableSlots = new HashMap<>();
            for (String internalName : internalNames) {
                internalAvailableSlots.put(internalName, convert2D(arr));
            }

            // internal available slots is done
            int []externalArray1 = new int [numberOfDays*15];
            int []externalArray2 = new int [numberOfDays*15];
            int []externalArray3 = new int [numberOfDays*15];

            for (int i = 0; i < 15; i++) {

                externalArray1[i] = 1;
            }
            for (int i = 15; i <30 ; i++) {

                externalArray2[i] = 1;
            }
            for (int i = 30; i <45 ; i++) {

                externalArray3[i] = 1;
            }
            HashMap<String, int[][]> externalAvailableSlots = new HashMap<>();
            int c =0;
            for (String externalName : externalNames) {
                if (c % 3 ==0)
                externalAvailableSlots.put(externalName, convert2D(externalArray1));
                else if (c % 3 ==1)
                    externalAvailableSlots.put(externalName, convert2D(externalArray2));
                else
                    externalAvailableSlots.put(externalName, convert2D(externalArray3));
                c++;

            }
            // external available slots is done
            Arrays.sort(numberOfSlots);
            System.out.println(Arrays.toString(numberOfSlots));



            rooms.put("room1", new String[numberOfDays][15]); // 10 is the number of days and 15 is the number of slots
            for (int i = 0; i <= 11; i++) {
                rooms.put("room" + (i + 1), new String[numberOfDays][15]);
            }
            // rooms is done


            ArrayList<pentaTuple> ans = tabulate(studentsToBeAssigned, externalAvailableSlots, internalAvailableSlots, numberOfSlots);
            System.out.println(ans);
            int cnt = 0;
            for (pentaTuple an : ans) {
                if (an.room == null)
                    cnt++;
            }
//            for (String s : rooms.keySet()) {
//                System.out.println(Arrays.deepToString(rooms.get(s)));
//            }
            System.out.println(cnt);
            System.out.println(notAssignedStudents);
            System.out.println(notAssignedStudents.size());
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    static ArrayList<Integer> notAssignedStudents = new ArrayList<>();
    static HashMap<String, String[][]> rooms = new HashMap<>();

    public static ArrayList<pentaTuple> tabulate(ArrayList<triple> studentsToBeAssigned, HashMap<String, int[][]> externalAvailableSlots
            , HashMap<String, int[][]> internalAvailableSlots, Pair[] numberOfSlots) {
        Arrays.sort(numberOfSlots);
        HashSet<Integer> studentsAssigned = new HashSet<>();
        ArrayList<pentaTuple> ans = new ArrayList<>();
        for (Pair numberOfSlot : numberOfSlots) {
            String external = numberOfSlot.x;
            int[][] externalSlots = externalAvailableSlots.get(external);
            for (int i = 0; i < externalSlots.length; i++) {
                boolean available = false;
                for (int j = 0; j < externalSlots[i].length; j++) {
                    if (externalSlots[i][j] == 1) {
                        available = true;
                        break;
                    }

                }

                if (available)
                    assign(i, external);
            }


        }
        for (triple triple : studentsToBeAssigned) {
            int studentNo = triple.studentNo;
            String name = triple.name;
            String topic = triple.topic;
            String external = triple.external;
            String internal = triple.internal;
            int[][] externalSlots = externalAvailableSlots.get(external);
            int[][] internalSlots = internalAvailableSlots.get(internal);
            here:
            for (int i = 0; i < externalSlots.length; i++) {
                for (int j = 0; j < externalSlots[i].length; j++) {
                    if (externalSlots[i][j] == 1) {
                        if (internalSlots[i][j] == 1) {
                            externalSlots[i][j] = 0;
                            internalSlots[i][j] = 0;
                            String room = getroom(external, i, j);
                            ans.add(new pentaTuple(studentNo, name, topic, external, internal, i + 1, j + 1, room));
                            studentsAssigned.add(studentNo);
                            break here;

                        }
                    }
                }
            }
            externalAvailableSlots.put(external, externalSlots);
            internalAvailableSlots.put(internal, internalSlots);

        }
        for (triple triple : studentsToBeAssigned) {
            int studentNo = triple.studentNo;
            if (!studentsAssigned.contains(studentNo)) {
                notAssignedStudents.add(studentNo);
            }
        }

        return ans;


    }

    private static String getroom(String external, int i, int j) {
        for (String s : rooms.keySet()) {
            String[][] room = rooms.get(s);

            if (room[i][j] != null && room[i][j].equals(external)) {
                return s;
            }
        }
        return null;
    }

    private static boolean assign(int idx, String external) {
        for (String s : rooms.keySet()) {
            String[][] room = rooms.get(s);
            String[] day = room[idx];
            boolean Empty = true;
            for (int i = 0; i < day.length; i++) {
                if (day[i] != null) {
                    Empty = false;
                    break;
                }
            }
            if (Empty) {
                for (int i = 0; i < day.length; i++) {
                    day[i] = external;
                }
                room[idx] = day;
                rooms.put(s, room);
                return true;
            }


        }
        return false;

    }

    public static int[][] convert2D(int[] arr) {
        int[][] ans = new int[arr.length / 15][15];
        for (int i = 0; i < arr.length; i++) {
            ans[i / 15][i % 15] = arr[i];
        }
        return ans;

    }


    static class Pair implements Comparable<Pair> {
        String x;
        int y;

        public Pair(String x, int y) {
            this.x = x;
            this.y = y;
        }

        public int compareTo(Pair o) {
            return o.y - this.y;
        }

        public String toString() {
            return x + " " + y;
        }

    }

    static class triple {
        int studentNo;
        String name;
        String topic;
        String external;
        String internal;

        public triple(int studentNo, String name, String topic, String external, String internal) {
            this.studentNo = studentNo;
            this.name = name;
            this.topic = topic;
            this.external = external;
            this.internal = internal;
        }

        public String toString() {
            return studentNo + " " + name + " " + topic + " " + external + " " + internal;
        }
    }

    static class pentaTuple {
        int studentNo;
        String name;
        String topic;
        String external;
        String internal;
        int day;

        int slot;
        String room;

        public pentaTuple(int studentNo, String name, String topic, String external, String internal, int day, int slot, String room) {
            this.studentNo = studentNo;
            this.name = name;
            this.topic = topic;
            this.external = external;
            this.internal = internal;
            this.day = day;
            this.slot = slot;
            this.room = room;
        }

            public String toString () {
                return studentNo + " " + name + " " + topic + " " + external + " " + internal + " " + day + " " + slot + " " + room;
            }



    }
}

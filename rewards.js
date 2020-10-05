var express=require("express");
var router=express.Router({mergeParams:true});
var Game=require("../models/games");
var Reward=require("../models/reward");
var middleware=require("../middleware");
var User=require("../models/user");

router.get("/",function(req,res){
    
    Game.find({},function(err,games){
        var flag=1;
        if(err){
        console.log("SOMETHING WENT WRONG");
        }else{

     res.render("prof",{flag:flag,games:games,user:req.user});
        }
        });
    });


router.get("/new",middleware.isLoggedIn,middleware.checkOwnership,function(req,res){
    
    Game.findById(req.params.id,function(err,games){
        if(err){
            console.log(games);
            console.log(err);
         
            }else{
                
                res.render("rewards/new",{games:games});
            }
    })  ; 

});

router.post("/",middleware.isLoggedIn,middleware.checkOwnership,function(req,res){
    Game.findById(req.params.id,function(err,games){
        if(err){
            console.log(err);
            res.redirect("/games");
            }else{
                
                Reward.create(req.body.reward,function(err,reward){
                   if(err)
                   {req.flash("error","something went wrong");
                       console.log(err);
                   }else{
                    reward.author.id=req.user._id;
                    reward.author.username=req.user.username;
                    reward.save();

                       console.log(reward);
                       games.rewards.push(reward);
                       games.save();
                       req.flash("success","successfully added reward");
                       res.redirect("/profile");
                   }
                }
                );
               
            }
    })  ; 
});

router.delete("/:id",middleware.isLoggedIn,middleware.checkOwnership,function(req,res){
    Reward.findByIdAndDelete(req.params.id,function(err,rewards){
        if(err){
            console.log(err);
        }else{
            if(rewards.game!="none"){
            Game.findById(rewards.gameid,function(err,games){
                if(err){
                    console.log(err);
                }else{
                   // console.log(rewards.gameid==req.params.id);
                   console.log(games.rewards[0]);
                    games.rewards.pop();
                    games.save();
                    
                }
            });}
            User.find({},function(err,users){
                if(err){
                    console.log(err);
                }
                else{
                    console.log("user rewards="+users);
                    users.forEach(function(use){
                    use.rewards.remove(req.params.id);
                    use.save();
                    });
                     
                }
            });
            res.redirect("/profile");
        }
    })
});

router.get("/:id/edit",middleware.isLoggedIn,middleware.checkOwnership,function(req,res){

    Reward.findById(req.params.id,function(err,rewards){
        
                    res.render("rewards/edit",{rewards:rewards});
    });
    
});

router.put("/:reward_id/update",middleware.isLoggedIn,middleware.checkOwnership,function(req,res){
console.log("enter");
    Reward.findByIdAndUpdate(req.params.reward_id,req.body.rewards,function(err,updatedReward){
        if(err){
            console.log(err);
            }else{
                res.redirect("/profile");
            }
    })  ; 
    });

    router.put("/:reward_id/unlock",middleware.isLoggedIn,function(req,res){
        console.log("enter");
                var unlock=true;
        var flag=2;
    User.findById(req.user._id,function(err,users){
            if(err){
                console.log(err);
                
                }else{
                    console.log("err");
                    Reward.findByIdAndUpdate(req.params.reward_id,req.body.rewards,function(err,reward){
                       if(err)
                       {
                           console.log(err);
                       }else{
                           
                           //reward.save();
                           console.log(reward);
                           users.rewards.push(reward);
                           users.save();
                           console.log(req.user);
                           res.render("games/getscore",{unlock:unlock});
                           
                       }
                    }
                    );
                   
                }
        })  ; 
            // Reward.findByIdAndUpdate(req.params.reward_id,req.body.rewards,function(err,updatedReward){
            //     if(err){
            //         console.log(err);
            //         }else{
            //             console.log(updatedReward.author.id);
            //             console.log(req.user);
            //             res.render("games/getscore",{unlock:unlock});
            //         }
            // })  ; 
            });

            router.put("/:reward_id/unlockextra",middleware.isLoggedIn,function(req,res){
                console.log("enter");
                        var unlock=true;
                var flag=2;
            User.findById(req.user._id,function(err,users){
                    if(err){
                        console.log(err);
                        
                        }else{
                            console.log("err");
                            Reward.findByIdAndUpdate(req.params.reward_id,req.body.rewards,function(err,reward){
                               if(err)
                               {
                                   console.log(err);
                               }else{
                                   
                                   //reward.save();
                                  
                                   res.redirect("/profile");
                                   
                               }
                            }
                            );
                           
                        }
                })  ; 
                    // Reward.findByIdAndUpdate(req.params.reward_id,req.body.rewards,function(err,updatedReward){
                    //     if(err){
                    //         console.log(err);
                    //         }else{
                    //             console.log(updatedReward.author.id);
                    //             console.log(req.user);
                    //             res.render("games/getscore",{unlock:unlock});
                    //         }
                    // })  ; 
                    });


module.exports=router;